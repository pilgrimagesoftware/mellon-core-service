__author__ = "Paul Schifferer <paul@schifferers.net>"


# from app.common import helpers as common_helpers
# from app.common import exceptions
# from app.core import helpers as core_helpers

# # from app.mod_github import helpers as github_helpers
# # from app.mod_github import worker as github_worker
# import logging
# import json





# def send_approval_message(payload):
#     logging.debug(f"send_approval_message({payload})")

#     is_submitted = common_helpers.validate_json_value(payload, "$.action", "submitted")
#     if not is_submitted:
#         raise exceptions.ApprovalException(
#             "Incoming webhook request was not a PR approval submission."
#         )

#     is_approved = common_helpers.validate_json_value(
#         payload, "$.review.state", "approved"
#     )
#     if not is_approved:
#         raise exceptions.ApprovalException(
#             "Incoming webhook request was not a PR approval."
#         )

#     # get PR submitter
#     submitter = common_helpers.get_json_value(payload, "$.pull_request.user.login")
#     if submitter is None:
#         raise exceptions.ApprovalException(
#             "No submitter username found in webhook payload."
#         )

#     message, attachments = github_helpers.build_approval_message(payload)
#     slack_user = core_helpers.get_slack_user(submitter)
#     bot.send_message(slack_user, message, attachments=attachments)


# def merge_pull_request(payload):
#     logging.debug(f"merge_pull_request({payload})")

#     common_helpers.validate_json_value(payload, "$.type", "interactive_message")
#     common_helpers.validate_json_value(payload, "$.callback_id", "pr_action")
#     common_helpers.validate_json_value(payload, "$.team.domain", "car-labs")

#     action = common_helpers.get_json_value(payload, "$.actions[0]")
#     logging.debug(f"action: {action}")
#     common_helpers.validate_json_value(action, "$.name", "merge")

#     action_value = common_helpers.get_json_value(action, "$.value")
#     logging.debug(f"action_value: {action_value}")
#     pr_info = json.loads(action_value)

#     author = str(common_helpers.get_json_value(pr_info, "$.author"))
#     logging.debug(f"author: {author}")
#     owner = str(common_helpers.get_json_value(pr_info, "$.owner"))
#     logging.debug(f"owner: {owner}")
#     repo = str(common_helpers.get_json_value(pr_info, "$.repo"))
#     logging.debug(f"repo: {repo}")
#     number = int(common_helpers.get_json_value(pr_info, "$.number"))
#     logging.debug(f"number: {number}")

#     github_worker.merge_pull_request(author, owner, repo, number)
