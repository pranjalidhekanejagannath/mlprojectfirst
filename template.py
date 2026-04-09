import os
from pathlib import Path 
import logging

logging.basicConfig(level=logging.INFO)

project_name="mlproject"
list_of_files=[
    ".github/workflows/.gitkeep",
    f"src/mlproject/__init__.py",
    f"src/mlproject/components/__init__.py",
    f"src/mlproject/components/data_ingestion.py",
    f"src/mlproject/components/data_transformation.py",
    f"src/mlproject/components/model_trainer.py",
    f"src/mlproject/components/model_monitoring.py",
    f"src/mlproject/pipelines/__init__.py",
    f"src/mlproject/pipelines/training_pipeline.py",
    f"src/mlproject/pipelines/prediction_pipeline.py",
    f"src/mlproject/exception.py",
    f"src/mlproject/logger.py",
    f"src/mlproject/utils.py",
    "main.py",
    "app.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py"

]

for filepath in list_of_files:
    filepath=Path(filepath)
    filedir,filename = os.path.split(filepath)
    if filedir!="":
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"Creating directory: {filedir} for file: {filename}")
        
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
        with open(filepath,'w') as f:
            pass
        logging.info(f"Creating file :{filename}")

    else:
        logging.info(f"{filename} already exists")