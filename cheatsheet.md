# Terraform(IaC)

## Terraform Commands

### Initialize

- **terraform init**: Initializes the provider, module version requirements, and backend configurations.
  - `terraform init -input=true`: You need to provide the inputs on the command line, else Terraform will fail.
  - `terraform init -lock=false`: Disable lock of Terraform state file (not recommended).
  - `terraform init -upgrade`: Upgrades Terraform modules and Terraform plugins.

- **terraform get**: Downloads and updates modules mentioned in the root module.

### Provision

- **terraform plan**: Determines the state of all resources and compares them with real or existing infrastructure. It uses Terraform state file data to compare and provider API to check.
  - `terraform plan -compact-warnings`: Provides the summary of warnings.
  - `terraform plan -out=path`: Saves the execution plan in the specified directory.
  - `terraform plan -var-file=abc.tfvars`: Uses a specific `terraform.tfvars` file specified in the directory.

- **terraform apply**: Applies the changes to a specific cloud such as AWS or Azure.
  - `terraform apply -backup=path`: Backs up the Terraform state file.
  - `terraform apply -lock=true`: Locks the state file.
  - `terraform apply -state=path`: Prompts to provide the path to save the state file or use it for later runs.
  - `terraform apply -var-file=abc.tfvars`: Uses the specified `terraform.tfvars` file containing environment-wise variables.
  - `terraform apply -auto-approve`: Does not prompt to approve the apply command.

- **terraform destroy**: Destroys Terraform-managed infrastructure or the existing environment created by Terraform.
  - `terraform destroy -auto-approve`: Does not prompt to approve the destroy command.

- **terraform console**: Provides an interactive console to evaluate expressions such as join or split commands.
  - `terraform console -state=path`: Path to the local state file.

### Modify Config

- **terraform fmt**: Formats the configuration files in the proper format.
  - `terraform fmt -check`: Checks the input format.
  - `terraform fmt -recursive`: Formats Terraform configuration files stored in subdirectories.
  - `terraform fmt -diff`: Displays the difference between the current and previous formats.

- **terraform validate**: Validates the Terraform configuration files.
  - `terraform validate -json`: Outputs in JSON format.

### Check Infra

- **terraform graph**: Generates a visual representation of the execution plan in graph form.
  - `terraform graph -draw-cycles`
  - `terraform graph -type=plan`

- **terraform output**: Extracts the values of an output variable from the state file.
  - `terraform output -json`
  - `terraform output -state=path`

### Manipulate State

- **terraform state list**: Lists all the resources present in the state file created or imported by Terraform.
  - `terraform state list -id=id`: Searches for a particular resource using resource ID in the Terraform state file.
  - `terraform state list -state=path`: Prompts to provide the path of the state file and then lists all resources in the Terraform state file.

- **terraform state show**: Shows attributes of specific resources.
  - `terraform state show -state=path`: Prompts to provide the path and then provides the attributes of specific resources.

- **terraform import**: Imports existing resources from infrastructure not created using Terraform into the Terraform state file, including them in Terraform's next run.

- **terraform refresh**: Reconciles the Terraform state file, syncing any manually or otherwise modified resources in the state file.

- **terraform state rm**: Removes resources from the Terraform state file without actually removing the existing resources.

- **terraform state mv**: Moves resources within the Terraform state file from one location to another.

- **terraform state pull**: Manually downloads the Terraform state file from a remote state to your local machine.

- **terraform state push**: Manually uploads the local state file to the remote state.

## Terraform command category-wise

| Initialize         | Provision        | Modify Config      | Check infra         | Manipulate State          |
|--------------------|------------------|--------------------|---------------------|---------------------------|
| terraform init     | terraform plan   | terraform fmt      | terraform graph     | terraform state list      |
| terraform get      | terraform apply  | terraform validate | terraform output    | terraform state show      |
| terraform destroy  | terraform console|                    |                     | terraform state mv/rm     |
|                    |                  |                    |                     | terraform state pull/push |

## Terraform commands walkthrough

#### Finding Terraform Version 
- To find out the Terraform version, run:
terraform -version

#### Initializing Terraform
- Initialize Terraform in the working directory with configuration files using:
terraform init

#### Planning Deployment
- Generate a blueprint of resources to be deployed with:
terraform plan

#### Validating Configuration
- Validate Terraform configuration files with:
terraform validate

#### Viewing State
- View human-readable output of the state file generated after planning:
terraform show

#### Listing Resources
- List all resources within the Terraform state file using:
terraform state list

#### Provisioning Resources
- Provision resources using:
terraform apply

#### Graphical Representation
- Obtain a graphical view of resources in configuration files with:
terraform graph

#### Destroying Resources
- Destroy provisioned resources with:
terraform destroy