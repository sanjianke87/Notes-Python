## Python 安装

### 安装 pyenv

[pyenv](https://github.com/yyuu/pyenv)
是 Python 版本管理器，用于在一台计算机中同时安装多个 Python 版本。

```bash
git clone https://github.com/yyuu/pyenv.git ~/.pyenv
echo 'export PYENV_ROOT="$HOME/.pyenv"'>> ~/.bashrc
echo 'export PATH="$PYENV_ROOT/bin:$PATH"'>> ~/.bashrc
echo 'eval "$(pyenv init -)"' >> ~/.bashrc
exec $SHELL -l
```

### 安装 anaconda

[anaconda](https://www.continuum.io/downloads)
是一个 Python 科学发行版，其自带了科学计算中常用的模块，省去了自己编译安装的痛苦。

```bash
pyenv install -l | grep anaconda3
pyenv install anaconda3-4.1.0 --verbose
pyenv global anaconda3-4.1.0
```

### 更新 anaconda 预安装的模块

```bash
conda update conda
conda update anaconda
conda update --all
```

### 使用 conda 安装模块

conda 是 anaconda 自带的包管理器。

```
# 安装 obspy
conda config --add channels obspy
conda install obspy
```

### 用 pip 安装模块

pip 是 Python 自带的包管理器。

```bash
pip install -r requirements.txt
```
