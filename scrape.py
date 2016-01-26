import github
import base64

g = github.Github("AUTH_TOKEN")

org = g.get_organization("18F")
orgRepos = org.get_repos()

for repo in orgRepos:
    try:
        about = repo.get_file_contents(".about.yml")
        readme = repo.get_readme() 
    except github.GithubException:
        continue

    print('Writing ' + repo.name + '...')
    readme_file = open('readmes/' + repo.name + '.md', 'wb')
    readme_file.write(base64.b64decode(readme.content))
    readme_file.close()

    about_file = open('abouts/' + repo.name + '.yml', 'wb')
    about_file.write(base64.b64decode(about.content))
    about_file.close()

