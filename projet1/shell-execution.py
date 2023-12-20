import os
import subprocess

# execution sans params
script_dir = os.path.dirname(__file__)
script_absolute_path = os.path.join(script_dir, "files/script.sh")

subprocess.call(['sh', script_absolute_path])

#execution avec params
param_script_absolute_path = os.path.join(script_dir, "files/parm.sh")
subprocess.call(['sh', param_script_absolute_path, 'param1 param2'])
