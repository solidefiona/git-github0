I realy missed how to correct this error after installing pytorch i can not use torch package bellow is the error displayed:

(base) tianwen@lut-Z10PE-D8-WS:~$ conda activate pytorch
(pytorch) tianwen@lut-Z10PE-D8-WS:~$ conda list
# here is some conda package list
pip                       21.2.4           py38h06a4308_0    defaults
pycparser                 2.20                       py_2    defaults
pyparsing                 3.0.4              pyhd3eb1b0_0    https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
pyqt                      5.9.2            py38h05f1152_4    https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
python                    3.8.12               h12debd9_0    defaults
python-dateutil           2.8.2              pyhd3eb1b0_0    https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
python_abi                3.8                      2_cp38    conda-forge
pytorch                   1.4.0               py3.8_cpu_0  [cpuonly]  https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/pytorch
pytorch-mutex             1.0                        cuda    https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/pytorch
pytz                      2021.3             pyhd3eb1b0_0    https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
zlib                      1.2.11               h7b6447c_3    defaults
zstd                      1.4.9                haebb681_0    defaults
(pytorch) tianwen@lut-Z10PE-D8-WS:~$ conda deactivate
(base) tianwen@lut-Z10PE-D8-WS:~$ conda activate
(base) tianwen@lut-Z10PE-D8-WS:~$ python
Python 3.9.7 (default, Sep 16 2021, 13:09:58) 
[GCC 7.5.0] :: Anaconda, Inc. on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import torch
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ModuleNotFoundError: No module named 'torch'
>>> 

#  that is the problem I need your help please!

    
