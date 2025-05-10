# GitHub Contribution Graph Writer

This tool automates commits to your GitHub repo to "draw" a string on your contribution graph.

## Usage

1. Set your string in `contrib_writer/config.py`.
2. Run `python main.py` regularly (e.g., via cron or Task Scheduler).
3. The script will commit on the correct days to "draw" your string.

**Warning:** This will make automated commits to this repo! 