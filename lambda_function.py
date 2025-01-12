import json

def lambda_handler(event, context):
    # TODO implement test
    return {
        'statusCode': 200,
        'body': json.dumps('New lambda code here by cicd ')
    }
