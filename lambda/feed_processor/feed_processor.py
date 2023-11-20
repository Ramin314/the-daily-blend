import os
import json
import boto3
import mysql.connector
from mysql.connector import Error

secretsmanager = boto3.client('secretsmanager')

def lambda_handler(event, context):
    db_credentials = get_secret()

    connection = mysql.connector.connect(
        host=db_credentials['host'],
        user=db_credentials['username'],
        password=db_credentials['password'],
        database=db_credentials['dbname']
    )

    try:
        if connection.is_connected():
            # Example: Process your RSS feed data here
            # ...
            return {
                'statusCode': 200,
                'body': json.dumps('RSS feeds processed successfully')
            }
    except Error as e:
        print("Error while connecting to MySQL", e)
        return {
            'statusCode': 500,
            'body': json.dumps('Error while processing feeds')
        }
    finally:
        if connection.is_connected():
            connection.close()

def get_secret():
    secret_name = 'PlanetScaleDBCredentials'
    response = secretsmanager.get_secret_value(SecretId=secret_name)
    secret = response['SecretString']
    return json.loads(secret)

