variable "tenant_id" {
  description = "Openstack ceph tenant id"
  type        = string
}

variable "auth_url" {
  description = "Openstack Keystone auth url"
  type        = string
}

variable "application_credential_id" {
  description = "Openstack ceph application credential id"
  type        = string
  sensitive   = true
}

variable "application_credential_secret" {
  description = "Openstack ceph application credential secret"
  type        = string
  sensitive   = true
}

variable "s3_endpoint" {
  description = "Openstack ceph s3 endpoint url"
  type        = string
}
