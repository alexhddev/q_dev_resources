from boto3 import resource

import os
import json
import time
import requests

s3_client = resource('s3')
bucket_name = os.environ['MESSAGES_BUCKET']

# simple handler for aws lambda
def handler(event, context):

    # print the requests version:
    print(requests.__version__)

    try:
        method = event['httpMethod']
        
        if method == 'GET':
            return get_messages()
        elif method == 'POST':
            return post_message(event)
        else:
            return {
                'statusCode': 405,
                'body': json.dumps('Method Not Allowed')
            }
    except Exception as e:
        print(e)
        return {
            'statusCode': 500,
            'body': json.dumps('Internal server error')
        }
    
def get_messages():
    # list all objects in the bucket
    bucket = s3_client.Bucket(bucket_name)
    objects = bucket.objects.all()

    # send the list of objects back to the client
    messages = [obj.key for obj in objects]
    return {
        'statusCode': 200,
        'body': json.dumps(messages)
    }



def post_message(event):
    if 'body'in event:
        body = event['body']
        # put the body in the s3 bucket
        bucket = s3_client.Bucket(bucket_name)
        key = str(int(time.time()*1000)) + '.json'  
        bucket.put_object(Key=key, Body=body)
        return {
            'statusCode': 200,
            'body': 'POST request handled'
        }
    return {
        'statusCode': 400,
        'body': 'Request body missing'
    }

        


