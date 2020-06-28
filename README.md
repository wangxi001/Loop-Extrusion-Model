# Loop Extrusion Mathematical Model
A mathematical model predicts CTCF interaction specificity based on loop extrusion model.

## Running model
An input file example for all CTCF pair within 1 Mb in GM12878 chromosome1 is provided.
The following command runs loop extrusion model with this input file at 1/[CTCF] = 8.5, w = 3, lambda = 3,000,000

python3 LEmodel.py GM12878_hg19_training_with_label_chr1.txt output 8.5 3 3000000


