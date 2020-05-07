import json
import boto3 
def lambda_handler(event, context):
    # TODO implement
    
    ImageName = event['ImageName']
    Lib = event['Lib']
    Bin = event['Bin']
    Dmidecode = event['Dmidecode']
    
    dynamodb = boto3.resource('dynamodb')
    table_service = dynamodb.Table('ONUGDB')
    response = table_service.scan()
    data = (response['Items'])
    Passphrase = None
    for item in data:
        if(item['ImageName'] == ImageName and item['Lib'] == Lib and item['Bin'] == Bin and item['Dmidecode'] == Dmidecode):
            Passphrase = item['Passphrase']
            

    return {
        'statusCode': 200,
        'body': Passphrase
    }

