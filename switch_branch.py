'''
Select and Checkout an Existing Branch:
    The heads attribute is used to select an existing branch named existing_branch.
    The checkout method is called on the selected branch.
    A message is printed to confirm that the current branch has been changed to existing_branch.
'''
import git  # Import the GitPython library

# Define the repository path
repo_path = 'D:/Repos/DevOps/python_script_git'

try:
    # Open the existing repository
    repo = git.Repo(repo_path)
    print(f'Repository opened at {repo_path}')

    # Select an existing branch
    existing_branch = repo.heads['existing_branch']
    existing_branch.checkout()
    print('Changed the current branch to "existing_branch"')
except git.exc.GitCommandError as git_error:
    print(f'Git command error: {git_error}')
except Exception as e:
    print(f'An error occurred: {e}')
