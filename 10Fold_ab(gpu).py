
import os

num = [0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9]

for a in num:
		command_1 = "./netinfer_gpu -method bnbi -nbi_type SUB DRUG TARGET -nbi_k 4 -command cv -cv_style nbi -cv_fold 10 -cv_type DRUG TARGET -cv_length 5 10 15 20 -cv_repeat 10 -cv_seed 12345 "
		command_2 = "-nbi_alpha %0.1f"%(a)
		for b in num:
			output_name_1 = "EVALUATION_INDICATOR_%0.1f_%0.1f.txt"%(a, b)
			output_name_2 = "ROC_CURVE_%0.1f_%0.1f.txt"%(a, b)
			output_name_3 = "PR_CURVE_%0.1f_%0.1f.txt"%(a, b)
			command_3 = command_2 + " -nbi_beta %0.1f -nbi_gamma 0 -training_set Global_DT.tsv+Global_DS.tsv -output "%(b)
			command_all = command_1 + command_3 + output_name_1 + output_name_2 + output_name_3
			#print (command_all)
			see = "a = " + str(a) + " " + "b = " + str(b)
			print (see)
			os.system(command_all)
