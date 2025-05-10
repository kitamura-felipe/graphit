import subprocess
from datetime import date

def make_dummy_change():
    with open("dummy.txt", "a") as f:
        f.write("Commit for contribution graph\n")

def commit_and_push(commit_date: date):
    subprocess.run(["git", "add", "dummy.txt"])
    subprocess.run([
        "git", "commit", "--date", commit_date.strftime("%Y-%m-%dT12:00:00"),
        "-m", f"Automated commit for contribution graph on {commit_date}"
    ])
    subprocess.run(["git", "push"]) 