import requests


def send_email(to, subject, attachment, template,**kwargs):
    """Function to send email using Mailgun API"""
    api_key = ""
    domain = ""
    url = f"https://api.mailgun.net/v3/{domain}/messages"
    print(kwargs.items())
    for key, value in kwargs.items():
        try:
            template = template.replace("{{" + key + "}}", value)
        except:
            pass
    print(attachment)
    if attachment:
      try:
        response = requests.post(
            url,
            auth=("api", api_key),
            files=[("attachment", open(attachment, "rb"))],
            data={
                "from": kwargs["from"].format(domain),
                "to": to,
                "subject": subject,
                "html": template,
            },
        )
      except:
        return send_email(to,subject,None,template,**kwargs)
    else:
        print("hey")
        response = requests.post(
            url,
            auth=("api", api_key),
            data={
                "from": kwargs["from"].format(domain),
                "to": to,
                "subject": subject,
                "html": template,
            },
        )
    if response.status_code == 200:
        return True
    else:
        return False
