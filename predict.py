import os

command = "./netinfer_gpu -method bnbi -nbi_type SUB COMPOUND+DRUG TARGET -nbi_k 6 -nbi_alpha 0.1 -nbi_beta 0.1 -nbi_gamma -0.5 -command predict -predict_type COMPOUND TARGET -predict_num 20 -training_set Global_DT.tsv +Global_DS.tsv+COVID_DS.tsv -output ./test.tsv"

os.system(command)
