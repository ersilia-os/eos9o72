# imports
import os
import csv
import sys
from urllib.request import urlretrieve
from rdkit.Chem import MolFromSmiles
from chemprop import featurizers, nn
from chemprop.data import BatchMolGraph
from chemprop.nn import RegressionFFN
from chemprop.models import MPNN
import torch

# parse arguments
input_file = sys.argv[1]
output_file = sys.argv[2]

# current file directory
root = os.path.dirname(os.path.abspath(__file__))

# for extra info, check this issue https://github.com/JacksonBurns/chemeleon/issues/16

@torch.no_grad
def chemeleon_fingerprint(smiles: list[str], model: MPNN, featurizer: featurizers.SimpleMoleculeMolGraphFeaturizer):  # i.e. get_embeddings
    bmg = BatchMolGraph([featurizer(MolFromSmiles(s)) for s in smiles])
    bmg.to(device=model.device)
    return model.fingerprint(bmg).numpy(force=True)


# read SMILES from .csv file, assuming one column with header
with open(input_file, "r") as f:
    reader = csv.reader(f)
    next(reader)  # skip header
    smiles_list = [r[0] for r in reader]

# Load model for evaluation
featurizer = featurizers.SimpleMoleculeMolGraphFeaturizer()
agg = nn.MeanAggregation()
chemeleon_mp = torch.load(os.path.join(root, "..", "..", "checkpoints", "chemeleon_mp.pt"), weights_only=True)
mp = nn.BondMessagePassing(**chemeleon_mp['hyper_parameters'])
mp.load_state_dict(chemeleon_mp['state_dict'])
model = MPNN(message_passing=mp, agg=agg, predictor=RegressionFFN())
model.eval()

# Run model
outputs = chemeleon_fingerprint(smiles_list, model, featurizer)

#check input and output have the same lenght
input_len = len(smiles_list)
output_len = len(outputs)
assert input_len == output_len

# write output in a .csv file
with open(output_file, "w") as f:
    writer = csv.writer(f)
    header = [f"dim_{str(i).zfill(4)}" for i in range(2048)]
    writer.writerow(header)
    for o in outputs:
        writer.writerow(o)
