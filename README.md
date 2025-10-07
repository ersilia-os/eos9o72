# CheMeleon embeddings

CheMeleon is a molecular foundation model pre-trained on deterministic molecular descriptors from the Mordred package, leveraging a Directed Message-Passing Neural Network to predict these descriptors in a noise-free setting.

This model was incorporated on 2025-07-01.Last packaged on 2025-08-29.

## Information
### Identifiers
- **Ersilia Identifier:** `eos9o72`
- **Slug:** `chemeleon`

### Domain
- **Task:** `Representation`
- **Subtask:** `Featurization`
- **Biomedical Area:** `Any`
- **Target Organism:** `Any`
- **Tags:** `Embedding`

### Input
- **Input:** `Compound`
- **Input Dimension:** `1`

### Output
- **Output Dimension:** `2048`
- **Output Consistency:** `Fixed`
- **Interpretation:** Vector representation of a molecule

Below are the **Output Columns** of the model:
| Name | Type | Direction | Description |
|------|------|-----------|-------------|
| dim_0000 | float |  | Dimension 0 of the CheMeleon embedding |
| dim_0001 | float |  | Dimension 1 of the CheMeleon embedding |
| dim_0002 | float |  | Dimension 2 of the CheMeleon embedding |
| dim_0003 | float |  | Dimension 3 of the CheMeleon embedding |
| dim_0004 | float |  | Dimension 4 of the CheMeleon embedding |
| dim_0005 | float |  | Dimension 5 of the CheMeleon embedding |
| dim_0006 | float |  | Dimension 6 of the CheMeleon embedding |
| dim_0007 | float |  | Dimension 7 of the CheMeleon embedding |
| dim_0008 | float |  | Dimension 8 of the CheMeleon embedding |
| dim_0009 | float |  | Dimension 9 of the CheMeleon embedding |

_10 of 2048 columns are shown_
### Source and Deployment
- **Source:** `Local`
- **Source Type:** `External`
- **DockerHub**: [https://hub.docker.com/r/ersiliaos/eos9o72](https://hub.docker.com/r/ersiliaos/eos9o72)
- **Docker Architecture:** `AMD64`, `ARM64`
- **S3 Storage**: [https://ersilia-models-zipped.s3.eu-central-1.amazonaws.com/eos9o72.zip](https://ersilia-models-zipped.s3.eu-central-1.amazonaws.com/eos9o72.zip)

### Resource Consumption
- **Model Size (Mb):** `34`
- **Environment Size (Mb):** `7438`
- **Image Size (Mb):** `7383.86`

**Computational Performance (seconds):**
- 10 inputs: `31.4`
- 100 inputs: `23.87`
- 10000 inputs: `375.77`

### References
- **Source Code**: [https://github.com/JacksonBurns/chemeleon/tree/main](https://github.com/JacksonBurns/chemeleon/tree/main)
- **Publication**: [https://arxiv.org/abs/2506.15792](https://arxiv.org/abs/2506.15792)
- **Publication Type:** `Preprint`
- **Publication Year:** `2025`
- **Ersilia Contributor:** [arnaucoma24](https://github.com/arnaucoma24)

### License
This package is licensed under a [GPL-3.0](https://github.com/ersilia-os/ersilia/blob/master/LICENSE) license. The model contained within this package is licensed under a [MIT](LICENSE) license.

**Notice**: Ersilia grants access to models _as is_, directly from the original authors, please refer to the original code repository and/or publication if you use the model in your research.


## Use
To use this model locally, you need to have the [Ersilia CLI](https://github.com/ersilia-os/ersilia) installed.
The model can be **fetched** using the following command:
```bash
# fetch model from the Ersilia Model Hub
ersilia fetch eos9o72
```
Then, you can **serve**, **run** and **close** the model as follows:
```bash
# serve the model
ersilia serve eos9o72
# generate an example file
ersilia example -n 3 -f my_input.csv
# run the model
ersilia run -i my_input.csv -o my_output.csv
# close the model
ersilia close
```

## About Ersilia
The [Ersilia Open Source Initiative](https://ersilia.io) is a tech non-profit organization fueling sustainable research in the Global South.
Please [cite](https://github.com/ersilia-os/ersilia/blob/master/CITATION.cff) the Ersilia Model Hub if you've found this model to be useful. Always [let us know](https://github.com/ersilia-os/ersilia/issues) if you experience any issues while trying to run it.
If you want to contribute to our mission, consider [donating](https://www.ersilia.io/donate) to Ersilia!
