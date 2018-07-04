- main.tf 
  contains for code provisioning resources
    - identify the latest ubuntu image
    - configures s3 backend to save/restore state (s2 backend resource should preexist)
    - uses default VPC for security group configuration
    - configures ssh public key to be read from a file
    - creates EC2 instance with the idenfied latest ubuntu image, associates the ssh public key
    - configures EC2 instance to be accessed via ssh/http/https from the provided subnet 

- vars.tf 
  contains the input parameters for configuring resources. All of them have defaults. The main configurable parameters are
    - instance_type
        flavor/instance type of the ami image. 
        default = t2.micro
    - instance_name
        name of the AWS EC2 instance to be created. 
        default = trusty
    - public_key_path
        path to the ssh public key in order to ssh to the EC instance after it is created ( as user "ubuntu" ) 
        default = ~/.ssh/id_rsa.pub
    - sec_group
        subnet from which the EC2 instance can be accessed via ssh/http/https
        default = 5.148.131.186/32
    - key_name
        name of the SSH Key pair
        default = trusty-user-key
- outputs.tf
    - image_id
        image id used for provisioning the instance
    - public_hostname
        hostname to be used to ssh to the instance
