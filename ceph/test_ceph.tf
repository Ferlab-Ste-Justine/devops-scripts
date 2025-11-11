resource "openstack_identity_ec2_credential_v3" "test" {}

resource "openstack_objectstorage_container_v1" "test" {
  name  = "test-bucket"
}

resource "null_resource" "script" {
  provisioner "local-exec" {
    command = "python3 test_s3.py -e ${var.s3_endpoint} -a ${openstack_identity_ec2_credential_v3.test.access} -s ${openstack_identity_ec2_credential_v3.test.secret} -b ${openstack_objectstorage_container_v1.test.name} > test_s3.log"
  }

  provisioner "local-exec" {
    when    = destroy
    command = "rm test_s3.log"
  }
}
