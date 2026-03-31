
# 创建专用的算法工程环境（推荐 Python 3.10+，稳定性最好）
```
conda env remove --name supply_chain_ai
conda create -n supply_chain_ai python=3.12 -y
conda activate supply_chain_ai
```
# 查看已经安装的包
```
conda list
```
# 添加清华大学的镜像源
```
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main/
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/conda-forge/
```

# 显示当前镜地址
```
conda config --show channels
```

# 报错
```
CondaToSNonInteractiveError: Terms of Service have not been accepted for the following channels. Please accept or remove them before proceeding:
```

## 解决方案
接受镜象服务条款
```
conda tos accept
```

# 更新到最新版本
```
conda update -n base -c https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/conda-forge conda
```
如果不行，请手动安装
```
安装conda 版本py313-26.1.1 https://www.anaconda.com/
```

# 清理缓存
sudo conda clean --all
# 安装mamba 提效
conda install mamba -n base

# 先安装解析引擎
conda install -n base conda-libmamba-solver -y
# 设置为全局默认引擎
conda config --set solver libmamba

mamba uninstall numpy

mamba install xgboost 
mamba install pandas  joblib -y