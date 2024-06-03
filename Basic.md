# Theortical Concepts

# Challanges without Iac
    1.Need to learn to code
    2.Don’t know the change impact.
    3.Need to revert the change
    4.Can’t track changes
    5.Can’t automate a resource
    6.Multiple environments for infrastructure
# Iac -> Terraform
    1.Does orchestration, not just configuration management
    2.Supports multiple providers such as AWS, Azure, GCP, DigitalOcean and many more
    3.Provide immutable infrastructure where configuration changes smoothly
    4.Uses easy to understand language, HCL (HashiCorp configuration language)
    5.Easily portable to any other provider
    6.Supports Client only architecture, so no need for additional configuration management on a server
# Core concepts
    1.Variables: Also used as input-variables, it is key-value pair used by Terraform modules to allow customization.
    2.Provider: It is a plugin to interact with APIs of service and access its related resources.
    3.Module: It is a folder with Terraform templates where all the configurations are defined
    4.State: It consists of cached information about the infrastructure managed by Terraform and the related configurations.
    5.Resources: It refers to a block of one or more infrastructure objects (compute instances, virtual networks, etc.), which are used in configuring and managing the infrastructure.
    6.Data Source: It is implemented by providers to return information on external objects to terraform.
    7.Output Values: These are return values of a terraform module that can be used by other configurations.
    8.Plan: It is one of the stages where it determines what needs to be created, updated, or destroyed to move from real/current state of the infrastructure to the desired state.
    9.Apply: It is one of the stages where it applies the changes real/current state of the infrastructure in order to move to the desired state.
# How Terraform Works? two main components:
    1.Terraform Core: Takes user-configured Terraform input and compares it with the current infrastructure state, determining the necessary actions (create, update, delete) to achieve the desired configuration
    2.Providers: Specific technology plugins (e.g., AWS, Azure, GCP) in Terraform's architecture, offering access to resources for different platforms, enabling users to provision infrastructure at various levels, such as creating AWS resources or deploying services in a Kubernetes cluster.
# How's that work?
    1.tf config file allows teams to describe their infrastructure in simple DSL
    2.terraform CLI creates, changes, and destroys these resources accordingly
# Basic CLI usage
    1.terraform plan to view the execution plan
    2.terraform apply to execute the plan
    3.terraform destroy to destroy infrastructure
# tfstate -> Terraform saves record of infrastructure state in JSON
    1.current state lives in terraform.tfstate
    2.backup of previous state lives in terraform.tfstate.backup
# CRUD lifecycle
    plan + apply resolve what is requested with what exists, using .tf, provider APIs, and tfstate.
# Life Cycle -> init, plan, apply, and destroy.
    1.Terraform init initializes the working directory which consists of all the configuration files
    2.Terraform plan is used to create an execution plan to reach a desired state of the infrastructure. Changes in the configuration files are done in order to achieve the desired state.
    3.Terraform apply then makes the changes in the infrastructure as defined in the plan, and the infrastructure comes to the desired state.
    4.Terraform destroy is used to delete all the old infrastructure resources, which are marked tainted after the apply phase.

