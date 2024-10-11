'''
    mkdir my_project
    cd my_project
    Virtualenv my_project_env  or conda create --name my_project_env flask sqlalchemy numpy pandas
    press y
    source /my_project_env/bin/activate 
    
    conda env export > environment.yaml
    cat environment.yaml
    
    replicate the environment
    
    conda env create -f environment.yaml
    conda env list
    
'''