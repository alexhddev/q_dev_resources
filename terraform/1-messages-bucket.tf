resource "random_pet" "messages_bucket_name" {
  prefix  = "messages-bucket-"
  length = 2
}

resource "aws_s3_bucket" "messages_bucket" {
  bucket = random_pet.messages_bucket_name.id
  force_destroy = true
}