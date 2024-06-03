# Push to a remote Repository
# origin = repo.remote(name='origin')
# origin.push()
import git  # Import the GitPython library

# Define the repository path
repo_path = "repo_path"

try:
    # Open the existing repository
    repo = git.Repo(repo_path)
    print(f'Repository opened at {repo_path}')

    # Define the remote repository
    origin = repo.remote(name='origin')
    print('Remote "origin" defined')

    # Checkout the existing branch (e.g., 'main')
    existing_branch = repo.heads['main']
    existing_branch.checkout()
    print('Checked out to branch "main"')

    # Commit changes to the branch
    repo.index.commit('Initial commit on new branch')
    print('Committed successfully')

    # Push changes to the remote repository
    origin.push()
    print('Pushed changes to origin')
except git.exc.GitCommandError as git_error:
    print(f'Git command error: {git_error}')
except Exception as e:
    print(f'An error occurred: {e}')

