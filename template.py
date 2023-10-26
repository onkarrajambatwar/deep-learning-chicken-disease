import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]:%(message)s:')



project_name = 'classifier'


list_of_files =[
    ".github/workflow/.getkeep",
    f"src={project_name}/__init__.py",
    f"src={project_name}/components/__init__.py",
    f"src={project_name}/utils/__init__.py",
    f"src={project_name}/config/__init__.py",
    f"src={project_name}/config/configuration/__init__.py",
    f"src={project_name}/pipeline/__init__.py",
    f"src={project_name}/entity/__init__.py",
    f"src={project_name}/constant/__init__.py",
    "config/config.yaml",
    "dvc.yaml",
    "params.yaml",
    "requirments.txt",
    "setup.py",
    "research/trials.ipynb"
]

for filePath in list_of_files:
    filePath = Path(filePath)
    file_dir, filename = os.path.split(filePath)
    
    if file_dir != '':
        os.makedirs(file_dir, exist_ok=True)
        logging.info('Create basic component dir')
        
    if (not os.path.exists(filePath) or (os.path.getsize(filePath)> 0)):
        with open(filePath, 'w') as f:
            pass
            logging.info('Creating empty file.')
            
    else:
        logging.info('File is already exists')
        
    