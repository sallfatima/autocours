provider "aws" {
  region = var.region
}

resource "aws_instance" "autocours" {
  ami           = var.ami
  instance_type = var.instance_type

  tags = {
    Name = "autocours-instance"
  }
}
