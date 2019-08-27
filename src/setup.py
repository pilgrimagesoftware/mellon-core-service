__author__ = "Paul Schifferer <paul@schifferers.net>"


from app.core import helpers as core_helpers
from app.core import objects


def initialize():
    # Build the database:
    core_helpers.setup_database()

    process_chat_users()


def process_chat_users():
    print("Getting users from Slack...")
    objects.slack_bot.get_users()

    print("Getting users from Discord...")
    # discord_bot.get_users()

    # TODO: reconcile admin users with user lists from Slack/Discord
