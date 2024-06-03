# Correct File Paths: Ensure that the file paths are correct and the files exist in the specified paths.
# Branching: If you intend to commit to a new branch, you should create and checkout the branch before committing.
# Error Handling: Adding basic error handling can make the script more robust.
'''
Import Libraries: The script imports the necessary git and os libraries.
Define Repository Path: The path to the local repository is defined.
Initialize Repository: The repository is initialized using git.Repo(repo_path).
Define File Paths: Full paths to the files to be added are constructed using os.path.join.
Add Files to Index: The files are added to the repository index.
Commit Changes: The changes are committed with a message.
Error Handling: Basic error handling is added to catch and print any exceptions that occur during the process.
'''

import os  # Importing os library for file path operations
import git  # Importing git library for Git operations

# Define the path to the local repository
repo_path = 'D:/Repos/DevOps/python_script_git'
repo = git.Repo(repo_path)  # Initializing the repository using the given path

# Define the file names to be added
file1 = 'D:/Repos/DevOps/python_script_git/sample1.html'
file2 = 'D:/Repos/DevOps/python_script_git/sample2.html'

# Construct the full paths to the files using os.path.join
file1_path = os.path.join(repo_path, file1)
file2_path = os.path.join(repo_path, file2)

try:
    # Add the files to the repository index
    repo.index.add([file1_path, file2_path])
    print('Files added successfully')

    # Commit the changes with a commit message
    repo.index.commit("Initial Commit Changes")
    print('Commit successful')
except Exception as e:
    print(f'An error occurred: {e}')  # Print the error message if an exception occurs