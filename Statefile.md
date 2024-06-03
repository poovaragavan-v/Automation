# Terraform State File

### Overview
- Purpose: Stores details of resources managed by Terraform.
- File Name: **terraform.tfstate**
- Format: JSON
- Contents: Full details of resources defined in Terraform code.

### Creation
- Created by: terraform apply command.
- Contains: Details of resources defined in Terraform configuration files.

### Managing State File
- Backup File: **terraform.tfstate.backup**
- Serves as a version of the state file.
- Helpful for reverting changes or understanding previous configurations.

### State File Structure
- terraform_version: Version of Terraform used.
- outputs: Outputs defined in Terraform code.
- resources: Detailed information of resources.

### Managing State File
- Storage: Preferably stored in a shared storage system (e.g., GitHub, S3).
- Locking: Prevent simultaneous modifications by team members using S3 and DynamoDB.
- Terraform Cloud: Offers native locking mechanism for state files.

### Terraform Workspaces
- Purpose: Isolates state files for different environments.
- Usage: Use separate workspaces for each environment (e.g., production, staging).
- Benefits: Prevents accidental modifications across environments.

### Basic Commands for Terraform State
- terraform state list: Lists all objects present in the state file.
- terraform state show <resource_name>: Shows details about a specific resource.
- terraform state mv <resource_name>: Renames a resource in the state file.
- terraform state pull: Outputs current state to standard out.
- terraform state push: Updates remote state from local.