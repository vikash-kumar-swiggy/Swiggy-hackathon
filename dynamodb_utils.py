import boto3
import pandas as pd
from boto3.dynamodb.conditions import Key, Attr

def configure_dynamodb():
    # Configure AWS credentials (or use environment variables/IAM roles)
    dynamodb = boto3.resource('dynamodb',
                             region_name='your-region',
                             aws_access_key_id='your-access-key',
                             aws_secret_access_key='your-secret-key')
    return dynamodb

def execute_query(query_type, table_name, query_params, dynamodb=None):
    if not dynamodb:
        dynamodb = configure_dynamodb()

    table = dynamodb.Table(table_name)
    result = None

    if query_type == 'scan':
        result = table.scan(**query_params)
    elif query_type == 'query':
        result = table.query(**query_params)
    elif query_type == 'get_item':
        result = table.get_item(**query_params)

    # Convert DynamoDB response to pandas DataFrame for visualization
    items = result.get('Items', [])
    df = pd.DataFrame(items)
    return df
