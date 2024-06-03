'''
Pull Latest Changes:
    origin.pull(): Pull the latest changes from the remote repository.
Verify the Pull:
    last_commit = repo.head.commit: Get the last commit from the repository.
'''
import git  # Import the GitPython library

# Define the repository path
repo_path = "D:/Repos/DevOps/python_script_git"

try:
    # Open the existing repository
    repo = git.Repo(repo_path)
    print(f'Repository opened at {repo_path}')

    # Define the remote repository
    origin = repo.remote(name='origin')
    print('Remote "origin" defined')

    # Pull the latest changes from the remote repository
    origin.pull()
    print('Pulled changes from the origin')
    
    # Verify the pull by listing the last commit
    last_commit = repo.head.commit
    print(f'Last commit: {last_commit.message} by {last_commit.author}')
except git.exc.GitCommandError as git_error:
    print(f'Git command error: {git_error}')
except Exception as e:
    print(f'An error occurred: {e}')
