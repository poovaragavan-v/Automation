'''

Create a New Branch:
    The create_head method is used to create a new branch named new_branch.
    A message is printed to confirm that the new branch has been created.
Checkout the New Branch:
    The new branch is checked out using the checkout method.
    A message is printed to confirm that the current branch has been changed to new_branch.

    
'''

import git  # Import the GitPython library

# Define the repository path
repo_path = 'repo_path_url'

try:
    # Initialize or open the existing repository
    repo = git.Repo(repo_path)
    print(f'Repository opened at {repo_path}')

    # Create a new branch
    new_branch = repo.create_head('new_branch')
    print('New branch "new_branch" created')

    # Checkout the new branch
    new_branch.checkout()
    print('Changed the current branch to "new_branch"')
except git.exc.GitCommandError as git_error:
    print(f'Git command error: {git_error}')
except Exception as e:
    print(f'An error occurred: {e}')