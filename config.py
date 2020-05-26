import yaml
import os, sys

# Load the main config file
with open(os.path.join(sys.path[0], 'config.yaml'), "r") as f:
    cfg = yaml.load(f, Loader=yaml.FullLoader)

discord_token = cfg['discord']['token']
discord_server = cfg['discord']['server_id']