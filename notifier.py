import smtplib, ssl
import os

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


port = 587
smtp_server = os.environ.get("SMTP_SERVER")
SENDER_EMAIL = os.environ.get("SENDER_EMAIL")
SENDER_PASSWORD = os.environ.get("SENDER_PASSWORD")
RECEIVER_EMAIL = os.environ.get("RECEIVER_EMAIL")
TEXT = os.environ.get("MSG")

def send_email():
    message = MIMEMultipart("alternative")
    message["Subject"] = "message from pipeline"
    message["From"] = SENDER_EMAIL
    message["To"] = RECEIVER_EMAIL

    text = """\
        This is msg is from the gitea pipeline
    """
    text = TEXT

    part1 = MIMEText(text, "plain")
    message.attach(part1)
    # Create a secure SSL context
    context = ssl.create_default_context()

    # Try to log  to server and send email
    try:
      server = smtplib.SMTP(smtp_server, port)
      server.ehlo()
      server.starttls(context=context)
      server.ehlo()
      server.login(SENDER_EMAIL, SENDER_PASSWORD)
      server.sendmail(SENDER_EMAIL, RECEIVER_EMAIL, message.as_string())
    except Exception as e:
      print(e)
    finally:
      server.quit()


if __name__ == "__main__":
    send_email()
