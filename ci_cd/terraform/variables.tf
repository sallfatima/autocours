variable "region" {
  description = "AWS region"
  default     = "us-east-1"
}

variable "ami" {
  description = "AMI ID pour l'instance"
}

variable "instance_type" {
  description = "Type d'instance"
  default     = "t2.micro"
}
