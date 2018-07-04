# Configure the AWS Provider
provider "aws" {
  region = "${var.aws_region}"
}

terraform {
  backend "s3" {
    bucket  = "shyam-terraform-1"
    region  = "us-east-1"
    key     = "SRE-phase4-tech-challenge-v02/terraform.tfstate"
    encrypt = true
    #enable in a team environment in order to lock/unlock
    #dynamodb_table = "terraform_dev"
  }
}

data "aws_ami" "ubuntu" {
    most_recent = true

    filter {
        name   = "name"
        values = ["ubuntu/images/hvm-ssd/ubuntu-xenial-16.04-amd64-server-*"]
    }

    filter {
        name   = "virtualization-type"
        values = ["hvm"]
    }

    owners = ["099720109477"] # Canonical
}

resource "aws_key_pair" "auth" {
  key_name   = "${var.key_name}"
  public_key = "${file(var.public_key_path)}"
}
resource "aws_instance" "trusty" {
    ami           = "${data.aws_ami.ubuntu.id}"
    instance_type = "${var.instance_type}"

  # The name of our SSH keypair we created above.
  key_name = "${aws_key_pair.auth.id}"

  # Our Security group to allow HTTP and SSH access
  vpc_security_group_ids = ["${aws_security_group.default.id}"]
  
    tags {
        Name = "${var.instance_name}"
    }
}

resource "aws_default_vpc" "default" {
    tags {
        Name = "Default VPC"
    }
}
# Our default security group to access
# the instances over SSH and HTTP
resource "aws_security_group" "default" {
  name        = "trusty_sg"
  description = "Security group for Trusty"
  vpc_id      = "${aws_default_vpc.default.id}"

  # SSH access from sg_host
  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["${var.sec_group}"]
  }

  # HTTP access from sg_host
  ingress {
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["${var.sec_group}"]
  }

  # HTTPS access from sg_host
  ingress {
    from_port   = 443
    to_port     = 443
    protocol    = "tcp"
    cidr_blocks = ["${var.sec_group}"]
  }

  # outbound internet access
  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

