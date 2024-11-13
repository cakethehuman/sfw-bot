from git import Repo, Remote

branch = "dev"
repo_url = "https://github.com/cakethehuman/sfw-bot"

repo = Repo(repo_url)
remote: Remote

try:
    remote = repo.remote('main')
except:
    remote = repo.create_remote('main', repo_url)

async def pull():
    current = repo.head.commit
    remote.fetch()
    if current != repo.head.commit:
        Repo.clone_from(repo_url, './live')