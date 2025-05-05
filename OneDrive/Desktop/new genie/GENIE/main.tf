provider "aws" {
  region = "us-east-1"
}

resource "aws_instance" "genie_ec2" {
  ami           = "ami-0c55b159cbfafe1f0"
  instance_type = "t2.medium"

  tags = {
    Name = "GENIE AIOCC Host"
  }
}

resource "aws_security_group" "genie_sg" {
  name        = "genie_sg"
  description = "Allow inbound access for GENIE dashboards"

  ingress {
    from_port   = 8501
    to_port     = 8501
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    from_port   = 5678
    to_port     = 5678
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    from_port   = 5432
    to_port     = 5432
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}