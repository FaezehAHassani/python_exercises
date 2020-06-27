$ pip3.7 list

# asked to upgrade
$ pip3.7 install --upgrade pip

$ sudo pip3.7 install virtualenv

# making a virtual environment
$ mkdir ~/.venvs
$ virtualenv --system-site-packages ~/.venvs/lpthw
$ . ~/.venvs/lpthw/bin/activate

(lpthw) Faezehs-MacBook-Pro:python_project faezeh$ mkdir projects
(lpthw) Faezehs-MacBook-Pro:python_project faezeh$ cd projects/
(lpthw) Faezehs-MacBook-Pro:projects faezeh$ mkdir skeleton
(lpthw) Faezehs-MacBook-Pro:projects faezeh$ cd skeleton
(lpthw) Faezehs-MacBook-Pro:skeleton faezeh$ mkdir bin FAEZEH tests docs
(lpthw) Faezehs-MacBook-Pro:skeleton faezeh$ touch FAEZEH/__init__.py
(lpthw) Faezehs-MacBook-Pro:skeleton faezeh$ touch tests/__init__.py


# check if "nose" is installed
$ python3.7
>>> help('modules')
# this lists all the modules, if nose is not there do the following in terminal, main depository
$ pip install nose
