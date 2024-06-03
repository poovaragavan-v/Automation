import git  # Import the GitPython library
import os   # Import the os library for file and directory operations
from git import Repo  # Import Repo from git for repository operations

# Initialize a new local repository
new_repo = Repo.init('D:/Repos/DevOps/python_script_git')
print('Initialized a new repository')

# Open an existing local repository
existing_repo = Repo('D:/Repos/DevOps/python_script_git')
print('Opened an existing repository')

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

# Repository URL and local directory
repo_url = 'https://github.com/ragsvp/DevOps_Py.git'
local_dir = 'D:/Repos/Py_DevOps'

# Clone the repository
clone_repo(repo_url, local_dir)