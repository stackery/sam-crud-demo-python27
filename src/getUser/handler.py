import boto3
import os
import json

def handler(message, context):
  print(message)

  userId = message['pathParameters']['id']

  print('Getting user %s from table %s' % (userId, os.environ['TABLE_NAME']))
  client = boto3.client('dynamodb')
  response = client.get_item(TableName = os.environ['TABLE_NAME'], Key = {'id': {'S': userId}})
  print('Done')

  return {
    'statusCode': 200,
    'headers': {},
    'body': json.dumps(response['Item'])
  }