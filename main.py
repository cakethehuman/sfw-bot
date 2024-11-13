from git import Repo, Remote
from pathlib import Path

branch = "dev"
repo_url = "https://github.com/cakethehuman/sfw-bot"
local_repo = Path("./")
local_live_repo = Path('./live')

def pull():
    repo = Repo(local_repo)
    repo.rev_parse(f'origin/{branch}')

    try:
        repo_live = Repo(local_live_repo)
        if repo.rev_parse != repo_live.rev_parse:
            Repo.clone_from(repo_url, local_repo, branch=branch)
    except:
        # Just clone immediately
        Repo.clone_from(repo_url, local_repo, branch=branch)
    
    local_live_repo.unlink(missing_ok=True)

pull()