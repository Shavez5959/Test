"""TEST FILE: intentional security problems for Bandit to detect.
Do NOT use this code in a real project."""
import hashlib
import pickle
import subprocess

import requests
import yaml

PASSWORD = "SuperSecret123!"                      # B105 hardcoded password


def run_command(user_input):
    # B602: subprocess with shell=True (command injection risk)
    subprocess.call("ls " + user_input, shell=True)


def calculate(expression):
    return eval(expression)                       # B307: use of eval


def load_data(raw_bytes):
    return pickle.loads(raw_bytes)                # B301: unsafe pickle


def hash_password(pw):
    return hashlib.md5(pw.encode()).hexdigest()   # B324: weak MD5 hash


def read_config(text):
    return yaml.load(text)                        # B506: unsafe yaml.load


def fetch(url):
    return requests.get(url, verify=False)        # B501: TLS verification off


def get_user(cursor, name):
    # B608: SQL built with string concatenation (SQL injection)
    cursor.execute("SELECT * FROM users WHERE name = '" + name + "'")


def start_server(app):
    app.run(host="0.0.0.0", debug=True)           # B104 / B201: bind all + debug
