data "archive_file" "js_message_lambda_zip" {
    type = "zip"
    source_dir = "${path.module}/js/src"
    output_path = "${path.module}/.terraform/js/src.zip"
}

# basic role for lambda
resource "aws_iam_role" "js_message_lambda_role" {
    name = "js-message-lambda-role"
    assume_role_policy = <<POLICY
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Action": "sts:AssumeRole",
      "Principal": {
        "Service": "lambda.amazonaws.com"
      },
      "Effect": "Allow",
      "Sid": ""
    }
  ]
}
POLICY
}

# attach to AWSLambdaBasicExecutionRole
resource "aws_iam_role_policy_attachment" "js_message_lambda_policy_attachment" {
    role = aws_iam_role.js_message_lambda_role.name
    policy_arn = "arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole"
}

resource "aws_lambda_function" "js_message_lambda" {
    function_name = "js-message-lambda"
    role = aws_iam_role.js_message_lambda_role.arn
    handler = "HandleMessage.handler"
    runtime = "nodejs20.x"
    filename = data.archive_file.js_message_lambda_zip.output_path
    source_code_hash = data.archive_file.js_message_lambda_zip.output_base64sha256
    environment {
        variables = {
            MESSAGES_BUCKET = aws_s3_bucket.messages_bucket.id
        }
    }
}