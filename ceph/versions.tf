terraform {
  required_providers {
    openstack = {
      source  = "terraform-provider-openstack/openstack"
      version = "= 1.52.1"
    }
    null = {
      source  = "hashicorp/null"
      version = "= 3.2.4"
    }
  }
  required_version = ">= 1.3.0"
}
