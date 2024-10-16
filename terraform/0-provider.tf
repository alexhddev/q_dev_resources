terraform {
  required_providers {
    aws = {
      source = "hashicorp/aws"
      version = "5.72.0"
    }
    random = {
      source  = "hashicorp/random"
      version = "3.6.3"  
    }
  }
}

provider "aws" {
  region = "eu-central-1"
}