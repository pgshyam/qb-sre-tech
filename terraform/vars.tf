variable "aws_region" {
  description = "AWS region to be used for provisioning resources"
  default = "us-east-1"
}

variable "public_key_path" {
  description = "Path to SSH public key"
  default = "~/.ssh/id_rsa.pub"
}

variable "key_name" {
  description = "Desired name of AWS key pair"
  default = "trusty-user-key"
}

variable "instance_name" {
  description = "Name of the EC2 Instance"
  default     = "trusty"
}

variable "instance_type" {
  description = "Instance Type of the EC2 Instance"
  default     = "t2.micro"
}

variable "sec_group" {
  description = "Security Group"
  default     = "5.148.131.186/32"
}
