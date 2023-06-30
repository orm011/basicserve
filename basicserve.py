import ray
from basicserve import app
import uvicorn
import os
import argparse

"""
deploys session server and exits. if it has been run before, when re-run it will re-deploy the current version.
"""

import argparse

parser = argparse.ArgumentParser(description="start server, init pool")
# parser.add_argument("--save_path", type=str, help="folder to save sessions in")
parser.add_argument("--num_gpus", type=int, default=2, help="gpus to use for pool")
args = parser.parse_args()

#os.makedirs(args.save_path, exist_ok=True)
#assert os.path.isdir(args.seesaw_root)
ray.init("auto", namespace="basicserve", log_to_driver=True)
uvicorn.run(app, host="127.0.0.1", port=8000, log_level="info")