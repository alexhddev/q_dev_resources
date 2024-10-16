resource "aws_apigatewayv2_api" "messages_api" {
    name = "messages-api"
    protocol_type = "HTTP"
}

# api stage
resource "aws_apigatewayv2_stage" "dev_stage" {
    api_id = aws_apigatewayv2_api.messages_api.id
    
    name = "dev"
    auto_deploy = true
}
