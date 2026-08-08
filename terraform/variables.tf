variable "region" {
  description = "AWS region to deploy in"
  type        = string
  default     = "us-east-1"
}

variable "instance_type" {
  description = "EC2 instance type"
  type        = string
  default     = "t2.micro"
}

variable "server_name" {
  description = "Name tag for the EC2 instance"
  type        = string
  default     = "devops-server-v2"
}
