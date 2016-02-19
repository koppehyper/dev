import requests, json

def lambda_handler(event, context):
    slack_token = 'xoxp-XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
    post_slack (slack_token, "", "#catcafe", "testuser", ":cat:")
    return "OK"

def post_slack(token, msg, channel, username, icon):
    api_baseuri = "https://slack.com/api"
    method = "chat.postMessage"
    uri = "%s/%s" % (api_baseuri, method)

    attachment = [
        {
            "fallback": "Required plain-text summary of the attachment.",
            "color": "#36a64f",
            "pretext": "Request Result from lambda",
            "title": "RESULT",
            "image_url": "https://http.cat/200.jpg",
            }
        ]
    attachments = json.dumps(attachment)


    param = {"token": token,
             "channel": channel,
             "text": msg,
             "username": username,
             "link_names": True,
             "icon_emoji": icon,
             "attachments" : attachments
             }

    res = requests.get(uri, params=param, verify=True)

