# Terraform CheatSheet for Reference

#  tf version
    $ terraform version
# tf init
    $ terraform init
    - Ask for input if necessary. If false, will error if input was required.
    $ terraform init -input=false
    - change the backend details using -backend-config option. 
    -reconfigure will reconfigure the backend, ignoring any saved configuration.
# tf plan
    $ terraform plan
    $ terraform plan -out plan.out
    - optionally save the plan to a file, which you can then pass to the apply
# tf get
    $ terraform get
    - Update already use -update=true
    $ terraform get -update=true
# tf apply
    $ terraform apply -> do the actual operation on the infrastructure resource
    $ terraform apply -auto-approve -> without confirmation(yes), auto-confirmation.

    Pass different variables or variable files.
    $ terraform plan -var="instancetype=t2.small"
    $ terraform plan -var-file="custom.tfvars

    Use -target option to target specific resources, modules, or collections of resources.
    $ terraform apply -target="azure_vm_Demo.objects"
# tf destroy
    $ terraform destroy -> delete all resource but with confirmation.
    $ terraform plan –destroy -> Deleteion plan
    $ terraform destroy -target="objects" -> -target to destroy a specific resources.
# tf refresh
    $ terraform refresh -> update the terraform state file
# tf show
    $ terraform show
# tf validate
    $ terraform validate
# tf providers
    $ terraform providers
# tf state
    $ terraform state    
    Sub Commands
    - list                List resources in the state
    $ terraform state list
    
    - mv                  Move an item in the state
    $ terraform state show azure_vm.demo
    
    - pull                Pull current state and output to stdout
    $ terraform state pull > terraform.tfstate
    
    - push                Update remote state from a local state file
    $ terraform state push

    - replace-provider    Replace provider in the state
    - rm                  Remove instances from the state
    - show                Show a resource in the state

# Terraform CheatSheet for Reference 3

# tf format
    $ terraform fmt
# tf taint
    $ terraform taint -> command is used to mark a resource as tainted.
    $ terraform taint <resource_type>.<resource_name>
    - Tainting a resource means indicating that it is considered "dirty" or "unreliable" and should be recreated during the next terraform apply operation.
# tf workspaces
    - Terraform Workspaces will help to manage same terraform configurations for different environments (eg: dev, staging, production) in the same project directory.
    
    # Check the workspace
    $ terraform workspace show
    
    # Create new workspace
    $ terraform workspace new dev
    
    # List all workspaces
    $ terraform workspace list
    
    # Switch to a specific workspace
    $ terraform workspace select dev

# tf graph
$ terraform graph -> It will generate the visual graph of your infra based on tf config.
Reference Link -> https://marketplace.visualstudio.com/items?itemName=adamiBs.terraform-live-graph#:~:text=Open%20Visual%20Studio%20Code.,Restart%20Visual%20Studio%20Code.
