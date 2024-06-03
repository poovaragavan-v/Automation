import git  # Import the GitPython library
import os   # Import the os library for file and directory operations
from git import Repo  # Import Repo from git for repository operations

# Function to clone a repository
def clone_repo(repo_url, local_dir):
    """
    Clones a GitHub repository to a local directory.
    
    Parameters:
    repo_url (str): The URL of the GitHub repository to be cloned.
    local_dir (str): The local directory where the repository will be cloned.
    
    Returns:
    None
    """
    try:
        if not os.path.exists(local_dir):  # Check if the local directory exists
            os.makedirs(local_dir)  # Create the directory if it doesn't exist
        git.Repo.clone_from(repo_url, local_dir)  # Clone the repository
        print(f'Successfully cloned {repo_url} to {local_dir}')
    except Exception as e:
        print(f'Error cloning repository: {e}')


# Initialize a new local repository
new_repo = Repo.init('D:/Repos/DevOps/python_script_git')
print('Initialized a new repository')

# Open an existing local repository
existing_repo = Repo('D:/Repos/DevOps/python_script_git')
print('Opened an existing repository')

# Repository URL and local directory for cloning
repo_url = 'https://github.com/ragsvp/DevOps.git'
local_dir = 'D:/Repos/Py_DevOps'

# Clone the repository
clone_repo(repo_url, local_dir)

# Function to add and commit files to the repository
def add_and_commit_files(repo_path, files, commit_message):
    """
    Adds specified files to the repository index and commits them.
    
    Parameters:
    repo_path (str): The path to the local repository.
    files (list): List of file paths to be added and committed.
    commit_message (str): Commit message for the changes.
    
    Returns:
    None
    """
    try:
        repo = git.Repo(repo_path)  # Open the existing repository
        repo.index.add(files)  # Add files to the repository index
        print('Files added successfully')

        repo.index.commit(commit_message)  # Commit the changes with a message
        print('Commit successful')
    except Exception as e:
        print(f'An error occurred: {e}')

# Files to be added and committed
file1 = 'D:/Repos/DevOps/python_script_git/sample1.html'
file2 = 'D:/Repos/DevOps/python_script_git/sample2.html'
file1_path = os.path.join(local_dir, file1)
file2_path = os.path.join(local_dir, file2)

# Check if files exist before adding and committing
if os.path.exists(file1_path) and os.path.exists(file2_path):
    # Add and commit the files with a commit message
    add_and_commit_files(local_dir, [file1_path, file2_path], "Initial commit with sample files")
else:
    print('One or both files do not exist. Please check the file paths.')

# Define the repository path for branch operations
repo_path = 'D:/Repos/DevOps/python_script_git'

try:
    # Open the existing repository
    repo = git.Repo(repo_path)
    print(f'Repository opened at {repo_path}')

    # Create a new branch
    new_branch = repo.create_head('new_branch')
    print('New branch "new_branch" created')

    # Checkout the new branch
    new_branch.checkout()
    print('Changed the current branch to "new_branch"')

    # Select an existing branch (if needed)
    existing_branch = repo.heads['existing_branch']
    existing_branch.checkout()
    print('Changed the current branch to "existing_branch"')

    # Define the remote repository for pulling changes
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