import sys,os
from sklearn.metrics import make_scorer, average_precision_score, f1_score, precision_recall_curve
from math import pow, exp

f_in = open(sys.argv[1],'r')
f_out = open(sys.argv[2],'w')

w_ori = float(sys.argv[3])
w_kd = float(sys.argv[4])
lambda_ = float(sys.argv[5])

p_dict = {}
n = 0
kd = 0.0

for l in f_in:
	n = n+1
	i = l.strip().split()
	p_dict[int(i[4])] = [i[0],(int(i[1])+int(i[2]))/2,float(i[3])]
	kd = kd+float(i[3])
kd = kd/n

y_true = []
y_pred = []

f_pair = open(sys.argv[1]+'_training_with_label.txt')
l = f_pair.readline()
f_out.write(l.strip()+'\tchr\tp12\torientation\tprocessivity\tCTCF_window\n')

for l in f_pair:
	if(int(i[4])<0):
		continue
	i = l.strip().split()
	CTCF_w = 1
	p12 = (float(i[2])/(float(i[2])+kd*w_kd))*(float(i[3])/(float(i[3])+kd*w_kd))
	ori = pow(w_ori,(int(i[5])-int(i[7])-2)/2)
	processicivity = exp(-float(i[4])/lambda_)

	for k in range(int(i[0])+1,int(i[1])):
		CTCF_w = CTCF_w * (1 - p_dict[k][2]/(p_dict[k][2]+kd*w_kd))
	f_out.write('{}\t{}\t{}\t{}\t{}\t{}\n'.format(l.strip(),p_dict[int(i[0])][0],p12,ori,processicivity,CTCF_w))

	if(i[9] != '-1' and float(i[6])>0 and float(i[8])>0):
		y_true.append(int(i[9]))
		y_pred.append(p12*ori*CTCF_w)

print('%.4f'%average_precision_score(y_true,y_pred))
