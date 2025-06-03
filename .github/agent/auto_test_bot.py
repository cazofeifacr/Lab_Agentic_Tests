import os

from datetime import datetime

import requests

from github import Github


GEMINI_API_KEY = os.environ["GEMINI_API_KEY"]
REPO_NAME = os.environ["GITHUB_REPO"]
PROMPT_URL = "https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent"

print("Initializing GitHub client")
gh = Github(os.environ["GITHUB_TOKEN"])
repo = gh.get_repo(REPO_NAME)