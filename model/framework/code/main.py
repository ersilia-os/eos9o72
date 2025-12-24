# imports
import os
import sys
import numpy as np
from chemeleon_fingerprint import CheMeleonFingerprint
from ersilia_pack_utils.core import read_smiles, write_out

# parse arguments
input_file = sys.argv[1]
output_file = sys.argv[2]

# current file directory
root = os.path.dirname(os.path.abspath(__file__))

# for extra info, check this issue https://github.com/JacksonBurns/chemeleon/issues/16

# read input
_, smiles_list = read_smiles(input_file)

# Run model
chemeleon_fingerprint = CheMeleonFingerprint()
outputs = chemeleon_fingerprint(smiles_list)

#check input and output have the same lenght
input_len = len(smiles_list)
output_len = len(outputs)
assert input_len == output_len

header = [f"dim_{str(i).zfill(4)}" for i in range(2048)]

# write output in a .csv file
write_out(outputs, header, output_file, np.float32)
