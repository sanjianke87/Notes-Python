# Python学习笔记

## 安装

1. 安装 [pyenv](https://github.com/yyuu/pyenv)
   ```bash
   git clone https://github.com/yyuu/pyenv.git ~/.pyenv
   echo 'export PYENV_ROOT="$HOME/.pyenv"'>> ~/.bashrc
   echo 'export PATH="$PYENV_ROOT/bin:$PATH"'>> ~/.bashrc
   echo 'eval "$(pyenv init -)"' >> ~/.bashrc
   exec $SHELL -l
   ```

2. 安装 [anaconda](https://www.continuum.io/downloads)
   ```bash
   pyenv install anaconda3-4.0.0 --verbose
   ```

3. 更新预安装的模块
   ```bash
   conda update conda
   conda update anaconda
   conda update --all
   ```

4. 使用 conda 安装模块
   ```bash
   sh ./conda-install.sh
   ```

4. 用 pip 安装模块
   ```bash
   pip install -r requirements.txt
   ```

## 我使用的工具

1. [thefuck](https://github.com/nvbn/thefuck): 自动校正命令行中敲错的命令
2. [ghp-import](https://github.com/davisp/ghp-import): 将某个目录下的内容复制并推送到远程的 `gh-pages` 分支
3. [pep8](https://github.com/PyCQA/pycodestyle): PEP8风格检查工具
4. [Jupyter](http://jupyter.org/)

## 我使用的模块

1. [numpy](http://www.numpy.org/): 多维数组操作

## 学习资源

1. [The Python Tutorial](https://docs.python.org/3.5/tutorial/index.html)
2. [PEP 8, for Humans](http://pep8.org/)
3. [Numpy Official Quickstart tutorial](http://docs.scipy.org/doc/numpy/user/quickstart.html)
4. [Scipy Lecture Notes](http://www.scipy-lectures.org/)
