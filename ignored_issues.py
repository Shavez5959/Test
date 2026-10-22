# Same kind of problem as bandit_issues.py, but this folder is listed in
# ignore_paths, so NO findings should be reported for this file.
import subprocess

subprocess.call("ls", shell=True)
password = "ThisShouldBeIgnored1"
