from contrib_writer.config import TARGET_STRING, START_DATE
from contrib_writer.grid import string_to_grid, grid_to_commit_days
from contrib_writer.commit import make_dummy_change, commit_and_push
from contrib_writer.scheduler import schedule_commit

def main():
    grid = string_to_grid(TARGET_STRING)
    commit_days = set(grid_to_commit_days(grid, START_DATE))
    def do_commit(today):
        make_dummy_change()
        commit_and_push(today)
    schedule_commit(commit_days, do_commit)

if __name__ == "__main__":
    main() 