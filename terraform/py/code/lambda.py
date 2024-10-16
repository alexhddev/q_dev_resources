

import os


bucket_name = os.environ['MESSAGES_BUCKET']

# simple handler for aws lambda
def handler(event, context):
    
    method = event['httpMethod']
    # handle get requests
    if method == 'GET':
        return get_messages()
    if method == 'POST':
        return post_message(event)
    else:
        return {
            'statusCode': 405,
            'body': 'Method Not Allowed'
        }
    
def get_messages():
    return {
        'statusCode': 200,
        'body': 'Hello from get'
    }
def post_message(event):
    return {
        'statusCode': 200,
        'body': 'Hello from post'
    }

