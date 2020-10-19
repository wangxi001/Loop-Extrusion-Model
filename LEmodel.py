import sys,os
from sklearn.metrics import average_precision_score
from math import pow, exp

f_peak = open(sys.argv[1],'r')
f_training = open(sys.argv[2],'r')
f_out = open(sys.argv[3],'w')

# Model parameters w_ori=w in Eq. 5, w_ctcf=a, and lambda
w_ori = float(sys.argv[4])
w_ctcf = float(sys.argv[5])
lambda_ = float(sys.argv[6])

peak_dict = {}
n = 0
ctcf = 0.0

# Build dictionary for all ChIP-seq CTCF peaks with binding strength and position, calculate average CTCF ChIP-seq signal
for l in f_peak:
	n = n+1
	i = l.strip().split()
	peak_dict[int(i[4])] = [i[0],(int(i[1])+int(i[2]))/2,float(i[3])]
	ctcf = ctcf+float(i[3])
ctcf = ctcf/n

y_true = []
y_pred = []

l = f_training.readline()
f_out.write(l.strip()+'\tchr\tp12\torientation\tprocessivity\tCTCF_window\tprediction\n')

# Read in ChIA-PET loop interaction training data
for l in f_training:

	if(int(i[4])<0):
		continue
	i = l.strip().split()
	lc = 1

# Calculate p_i*p_j, CTCF orientation and distance dependent processivivity
	p_ij = (float(i[2])/(float(i[2])+ctcf*w_ctcf))*(float(i[3])/(float(i[3])+ctcf*w_ctcf))
	ori = pow(w_ori,(int(i[5])-int(i[7])-2)/2)
	processicivity = exp(-float(i[4])/lambda_)

# Calculate loop competiton term
	for k in range(int(i[0])+1,int(i[1])):
		lc = lc * (1 - peak_dict[k][2]/(peak_dict[k][2]+ctcf*w_ctcf))

# Write predictions to output file
	prediction = p_ij * ori * lc
	f_out.write('{}\t{}\t{}\t{}\t{}\t{}\t{}\n'.format(l.strip(),peak_dict[int(i[0])][0],p_ij,ori,processicivity,prediction,lc))

# Calculate AUPRC of predictions
	if(i[9] != '-1' and float(i[6])>0 and float(i[8])>0):
		y_true.append(int(i[9]))
		y_pred.append(p_ij*ori*lc)

print('AUPRC: %.4f'%average_precision_score(y_true,y_pred))
