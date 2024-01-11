import os 
from pathlib import Path 
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

package_name = "src"

list_of_files = [
    ".github/workflows/.gitkeep",
    "{package_name}/__init__.py",
    "{package_name}/components/__init__.py",
    "{package_name}/components/data_ingestion.py",
    "{package_name}/components/data_transformation.py",
    "{package_name}/components/model_trainer.py",
    "{package_name}/components/model_evaluation.py",
    "{package_name}/pipeline/__init__.py",
    "{package_name}/pipeline/training_pipeline.py",
    "{package_name}/pipeline/prediction_pipeline.py",
    "{package_name}/utils/__init__.py",
    "{package_name}/utils/utils.py",
    "{package_name}/logger/__init__.py",
    "{package_name}/logger/logging.py",
    "{package_name}/exception/__init__.py",
    "{package_name}/exception/exception.py",
    "tests/unit/__init__.py",
    "tests/integration/__init__.py",
    "init_setup.sh",
    "requirements.txt",
    "requirements_dev.txt",
    "setup.py",
    "setup.cfg",
    "pyproject.toml",
    "tox.ini",
    "experiment/experiments.ipynb"
]

for filepath in list_of_files:
   filepath = Path(filepath)
   filedir, filename = os.path.split(filepath)

   if filedir !="":
      os.makedirs(filedir, exist_ok=True)
      logging.info(f"Creating directory; {filedir} for the file {filename}")

   if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
      with open(filepath, 'w') as f:
         pass
         logging.info(f"Creating empty file: {filepath}")

   else:
      logging.info(f"{filename} is already created")