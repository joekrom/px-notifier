import smtplib, ssl
import os

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


smtp_port = os.environ.get("INPUT_SMTP_PORT")
smtp_address = os.environ.get("INPUT_SMTP_ADDRESS")
sender_email_auth = os.environ.get("INPUT_USERNAME")
sender_password_auth = os.environ.get("INPUT_PASSWORD")
receiver_email = os.environ.get("INPUT_TO")
subject = os.environ.get("INPUT_SUBJECT")
body = os.environ.get("INPUT_BODY")
sender_email = os.environ.get("INPUT_FROM")
ssl_tls = os.environ.get("INPUT_SSL")


def send_email():
    # Check if any of the environment variables are empty or None
    if None in (smtp_port, smtp_address, sender_email_auth, sender_password_auth, receiver_email, sender_email) or '' in (smtp_port, smtp_address, sender_email_auth, sender_password_auth, receiver_email, sender_email):
             # writing to the buffer
            output = "One or more required environment variables are empty or not set."
            #io.write_to_output({"status": f"Error: {output}"})
            raise ValueError(output)

    message = MIMEMultipart("alternative")
    message["Subject"] = subject
    message["From"] = sender_email
    message["To"] = receiver_email

    text = """\
        default message from action
    """
    text = body

    part1 = MIMEText(text, "plain")
    message.attach(part1)
    # Create a secure SSL context
    context = ssl.create_default_context()

    # Try to log  to server and send email
    try:
      server = smtplib.SMTP(smtp_address, int(smtp_port))
      server.ehlo()
      if ssl_tls == 'true':
          server.starttls(context=context)
      server.ehlo()
      server.login(sender_email_auth, sender_password_auth)
      server.sendmail(sender_email, receiver_email, message.as_string())
    except Exception as e:
        output = "One or more required environment variables are empty or not set."
        #io.write_to_output({"status": f"Error: {output}"})
        print(e)
    finally:
      server.quit()


if __name__ == "__main__":
    send_email()
