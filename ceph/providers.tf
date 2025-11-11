provider "openstack" {
  tenant_id                     = var.tenant_id
  application_credential_id     = var.application_credential_id
  application_credential_secret = var.application_credential_secret
  auth_url                      = var.auth_url
  region                        = "RegionOne"
}
