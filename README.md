# Loop Extrusion Mathematical Model
A mathematical model predicts CTCF interaction specificity based on loop extrusion model.

Requires:

* Python (tested 3.7.3)
* sklearn (tested 0.21.2)

## Running model
Example training input files for all CTCF peaks and pairs within 1 Mb on GM12878 chromosome 1 are provided.

The following command runs loop extrusion model with this input file at w = 3, <K<sub>d</sub>>/[CTCF] = 8.5, \lambda = 3,000,000, and writes to a file named 'output'.

    python3 LEmodel.py GM12878_hg19_CTCF_chr1.bed GM12878_hg19_training_with_label_chr1.txt output 3 8.5 3000000

AUPRC on this example should be 0.6087.

## Authors
Wang Xi, Michael A Beer
