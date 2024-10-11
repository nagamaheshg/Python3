'''
    great resources is - pip help
    it shows command and options
    to view specific command  - pip help install
    pip search pympler
    pip install Pympler
    To view installed packages.
    pip list
    pip uninstall package_name
    to find out version is outdate 
    
    pip list -o or pip list --outdated
    
    To upgrade specific package:
    pip install -U setuptools
    
    pip freeze -> it's put all of our packages and version numbers in requirement format. to send this run the below command
    
    pip freeze > requirements.txt
    
    to view cat requirements.txt
    
    How would they install packages using pip?
    
    pip install -r requirements.txt
    
    # pip list for verifying all installed or not
    
    pip list --outdated
    
    to update each package manually it take lot of time waste so 
    pip freeze --local | grep -v '^\-e' | cut -d = -f 1 | xargs -nl pip install -U
    
'''