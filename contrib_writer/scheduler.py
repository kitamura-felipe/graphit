import schedule
import time
from datetime import date

def schedule_commit(commit_dates, commit_func):
    today = date.today()
    if today in commit_dates:
        commit_func(today) 