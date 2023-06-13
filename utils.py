import sys
import logging
import importlib
from pathlib import Path 

def load_plug(plug_name):
  path = Path(f"Aalok1/plugins/{plug_name}.py")
  name = "Aalok1.plugins.{}".format(plug_name)
  spec = importlib.util.spec_from_file_location(name, path)
  load = importlib.util.module_from_spec(spec)
  load.logger = logging.getLogger(plug_name)
  spec.loader.exec_module(load)
  sys.modules["Aalok1.plugins." + plug_name] = load
  print("Aalok1 loaded" + plug_name)