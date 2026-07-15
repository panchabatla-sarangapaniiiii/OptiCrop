# Launcher for OptiCrop
import os
import sys
import subprocess

app_dir = os.path.join(
    os.path.dirname(__file__),
    "5. Project_Development_Phase",
    "Application"
)

os.chdir(app_dir)
subprocess.run([sys.executable, "app.py"])