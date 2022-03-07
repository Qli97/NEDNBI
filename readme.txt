The latest version of NetInfer can be downloaded from http://lmmd.ecust.edu.cn/netinfer/. This binary executable file was compiled by GNU C++ compiler (version 4.8.5) with the support of NVIDIA CUDA toolkit (version 10.1), and has been tested on CentOS 7. 

1. training NEDNBI model
   run 10Fold_ab.py  #Find the optimal value of parameters α, β

   run 10Fold_c.py   #Find the optimal value of parameter γ

2. prediction for new diseases
   run predict.py   #predict for new diseases, in this study, we are predicting for COVID-19.
 