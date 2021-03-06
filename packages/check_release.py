from sys import argv

import requests
import yaml

with open(f"{argv[1]}/config.yml", "r") as stream:
    version = yaml.safe_load(stream).get("version", "")
    r = requests.get(f"https://pypi.org/project/{argv[1]}/{version}/")
    print(r.status_code)
