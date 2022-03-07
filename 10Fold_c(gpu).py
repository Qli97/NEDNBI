import os

num = [-0.1,-0.2,-0.3,-0.4,-0.5,-0.6,-0.7,-0.8,-0.9,-1,0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1]

for c in num:
        output_name_1 = "EVALUATION_INDICATOR_%0.1f.txt"%(c)
        output_name_2 = "ROC_CURVE_%0.1f.txt"%(c)
        output_name_3 = "PR_CURVE_%0.1f.txt"%(c)
        command_1 = "./netinfer_gpu -method bnbi -nbi_type SUB DRUG TARGET -nbi_k 4 -command cv -cv_style nbi -cv_fold 10 -cv_type DRUG TARGET -cv_length 5 10 15 20 -cv_repeat 10 -cv_seed 12345 "
        command_2= "-nbi_alpha 0.1 -nbi_beta 0.1 -nbi_gamma %0.1f  -training_set Global_DT.tsv+Global_DS.tsv -output "%(c)
        #input a,1-a,b,1-b,default:a=b=0.1
        command_all = command_1 + command_2 + output_name_1 + output_name_2 + output_name_3
        #print (command_all)
        see = "c = " + str(c)
        print (see)
        os.system(command_all)
