

import os


bucket_name = os.environ['MESSAGES_BUCKET']

# simple handler for aws lambda
def handler(event, context):
    print(bucket_name)
    return {
        'statusCode': 200,
        'body': 'Hello from Lambda!'
    }

