
# api gateway integration
resource "aws_apigatewayv2_integration" "messages_integration" {
    api_id = aws_apigatewayv2_api.messages_api.id
    integration_type = "AWS_PROXY"
    integration_uri = aws_lambda_function.py_message_lambda.invoke_arn
    integration_method = "POST"
}

# get route
resource "aws_apigatewayv2_route" "get_messages_route" {
    api_id = aws_apigatewayv2_api.messages_api.id
    route_key = "GET /messages"
    target = "integrations/${aws_apigatewayv2_integration.messages_integration.id}"
}

# post route
resource "aws_apigatewayv2_route" "post_messages_route" {
    api_id = aws_apigatewayv2_api.messages_api.id
    route_key = "POST /messages"
    target = "integrations/${aws_apigatewayv2_integration.messages_integration.id}"
}

# permissions for api gateway to invoke lambda
resource "aws_lambda_permission" "messages_api_lambda_permission" {
    statement_id = "AllowExecutionFromAPIGateway"
    action = "lambda:InvokeFunction"
    function_name = aws_lambda_function.py_message_lambda.function_name
    principal = "apigateway.amazonaws.com"
    source_arn = "${aws_apigatewayv2_api.messages_api.execution_arn}/*/*"
}

# output the api dev stage endpoint
output "messages_api_dev_stage_endpoint" {
    value = aws_apigatewayv2_stage.dev_stage.invoke_url
}
