import github
import base64

g = github.Github("GITHUB_TOKEN")

org = g.get_organization("18F")
orgRepos = org.get_repos()

for repo in orgRepos:
    try:
        gemfile = repo.get_file_contents("Gemfile")
    except github.GithubException:
        continue

    print('Writing ' + repo.name + '...')
    gemfile_file = open('gemfiles/' + repo.name, 'wb')
    gemfile_file.write(base64.b64decode(gemfile.content))
    gemfile_file.close()

