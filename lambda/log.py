import json
import boto3
from datetime import datetime, timedelta

def lambda_handler(event, context):
    # TODO implement

    dynamodb = boto3.resource('dynamodb')
    table_service = dynamodb.Table('ONUGLogs')
    date = str(datetime.now()) 
    Success= False
    try:
        table_service.put_item(
            Item={
                            'ImageName': event['ImageName'],
                            'TimeStamp': date ,
                            'Status': event['Status'],
                            'Title': event['Title'],
                            'Message': event['Message']
                }
                )
        Success=True
    except:
        print("Table update failed")

    return {
        'statusCode': 200,
        'body': Success
    }

