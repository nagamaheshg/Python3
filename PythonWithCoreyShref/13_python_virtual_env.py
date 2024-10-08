'''
Virtual venv is separate different python environments for different projects.

each of project in isolated environment. only dependencies and packages specific versions they need.
that virtual environment will do.

=> pip install virtualenv ==> to install virtual env
=> pip list 
=> mkdir Environments
=> cd Environments
=> Virtualenv project1_env
=> source project1_env/bin/activate
=> to view the which version of python using is ==> which python
=> which pip
=> pip install numpy
=> pip list
=> pip freeze --local > requirements.txt
=> deactivate => this command is used to deactivate virtual environment
=> To remove virtual environment => rm -rf project1_env

---------
let make another virtual environment 
virtualenv -p /usr/bin/python3.11 project_name
which python
python --version
pip install -r requirement.txt
deactivate  

'''