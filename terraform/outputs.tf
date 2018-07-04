output "image_id" {
    value = "${data.aws_ami.ubuntu.id}"
}

output "public_hostname" {
    value = "${aws_instance.trusty.public_dns}"
}