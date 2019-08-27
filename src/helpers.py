__author__ = "Paul Schifferer <paul@schifferers.net>"


from app.common import constants

# from app.core.worker import slack_bot

# from app.core.worker import discord_bot

# from app import db
import logging
import os, time
import json


# def get_slack_user(github_username):
#     item = db.get_item(TableName=constants.SLACK_GITHUB_MAP_TABLE_NAME,
#                        Key={
#                            'GitHubUsername': {
#                                'S': github_username,
#                            }
#                        },
#                        AttributesToGet=[
#                            'SlackUsername'
#                        ])
#     if item is None:
#         return None
#     if 'Item' not in item:
#         return None
#     if 'SlackUsername' not in item['Item']:
#         return None

#     return item['Item']['SlackUsername'].get('S')


# This will create the database in DynamoDB
def setup_database():
    # t = db.describe_table(TableName=constants.SLACK_GITHUB_MAP_TABLE_NAME)
    # if t is not None and 'Table' in t and 'TableName' in t['Table']:
    #     logging.info(f"Username mapping table found in AWS: {t}")
    # else:
    #     logging.info("Creating username mapping table.")
    #     db.create_table(
    #         AttributeDefinitions=[
    #             {
    #                 'AttributeName': 'GitHubUsername',
    #                 'AttributeType': 'S'
    #             },
    #             {
    #                 'AttributeName': 'SlackUsername',
    #                 'AttributeType': 'S'
    #             },
    #             {
    #                 'AttributeName': 'Updated',
    #                 'AttributeType': 'N'
    #             },
    #         ],
    #         TableName=constants.SLACK_GITHUB_MAP_TABLE_NAME,
    #         KeySchema=[
    #             {
    #                 'AttributeName': 'GitHubUsername',
    #                 'KeyType': 'HASH'
    #             },
    #         ],
    #         ProvisionedThroughput={
    #             'ReadCapacityUnits': 123,
    #             'WriteCapacityUnits': 123
    #         })

    logging.info("Populating table with seed data...")
    cwd = os.getcwd()
    print(f"cwd={cwd}")
    # with open("app/github_slack_usernames.json", 'r') as s:
    #     try:
    #         seed_data = json.load(s)
    #         for item in seed_data:
    #             if 'GitHubUsername' not in item:
    #                 continue

    #             record = db.update_item(TableName=constants.SLACK_GITHUB_MAP_TABLE_NAME,
    #                                     ExpressionAttributeNames={
    #                                         '#S': 'SlackUsername',
    #                                         '#U': 'Updated',
    #                                     },
    #                                     ExpressionAttributeValues={
    #                                         ':s': {
    #                                             'S': item['SlackUsername'],
    #                                         },
    #                                         ':u': {
    #                                             'N': str(int(time.time())),
    #                                         },
    #                                     },
    #                                     Key={
    #                                         'GitHubUsername': {
    #                                             'S': item['GitHubUsername'],
    #                                         },
    #                                     },
    #                                     ReturnValues='ALL_NEW',
    #                                     UpdateExpression='SET #S = :s, #U = :u')

    #     except:
    #         logging.exception("Error while trying to import seed data.")
