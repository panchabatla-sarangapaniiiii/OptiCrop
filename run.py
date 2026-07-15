# run.py - Launcher for OptiCrop (from Development Phase)
import os
import sys
import subprocess

# Run the app from the Application folder
app_dir = os.path.join(os.path.dirname(__file__), 'Application')
os.chdir(app_dir)

# Run app.py
subprocess.run([sys.executable, 'app.py'])
