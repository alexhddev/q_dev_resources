data "archive_file" "py_message_lambda_zip" {
    type = "zip"
    source_dir = "${path.module}/py/code"
    output_path = "${path.module}/.terraform/py/src.zip"
}

# basic role for lambda
resource "aws_iam_role" "py_message_lambda_role" {
    name = "py-message-lambda-role"
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
resource "aws_iam_role_policy_attachment" "py_message_lambda_policy_attachment" {
    role = aws_iam_role.py_message_lambda_role.name
    policy_arn = "arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole"
}

resource "aws_iam_role_policy_attachment" "py_message_lambda_role_policy_attachment" {
    role = aws_iam_role.py_message_lambda_role.name
    policy_arn = aws_iam_policy.messages_bucket_access_lambda_policy.arn
}

resource "aws_lambda_function" "py_message_lambda" {
    function_name = "py-message-lambda"
    role = aws_iam_role.py_message_lambda_role.arn
    handler = "lambda.handler"
    runtime = "python3.11"
    filename = data.archive_file.py_message_lambda_zip.output_path
    source_code_hash = data.archive_file.py_message_lambda_zip.output_base64sha256
    layers = [ aws_lambda_layer_version.layer_version.arn ]
    environment {
        variables = {
            MESSAGES_BUCKET = aws_s3_bucket.messages_bucket.id
        }
    }
}

resource "aws_lambda_layer_version" "layer_version" {
    layer_name = "py-message-lambda-layer"
    filename = data.archive_file.layer_archive.output_path
    source_code_hash = data.archive_file.layer_archive.output_base64sha256
    compatible_runtimes = ["python3.11"]
}

data "archive_file" "layer_archive" {
  type = "zip"
  source_dir = "${path.module}/py/layer"
  output_path = "${path.module}/.terraform/layer.zip"
  depends_on = [ null_resource.pip_install ]
}

resource "null_resource" "pip_install" {
  triggers = {
    shell_hash = "${sha256(file("${path.module}/py/requirements.txt"))}"
  }

  provisioner "local-exec" {
    command = "python3 -m pip install -r py/requirements.txt -t ${path.module}/py/layer/python"
  }
  
}