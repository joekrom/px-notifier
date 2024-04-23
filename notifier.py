import smtplib, ssl
import os
import re

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
# for validating an Email
regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'

smtp_port = os.environ.get("INPUT_SMTP_PORT")
smtp_address = os.environ.get("INPUT_SMTP_ADDRESS")
sender_email_auth = os.environ.get("INPUT_USERNAME")
sender_password_auth = os.environ.get("INPUT_PASSWORD")
receiver_email = os.environ.get("INPUT_TO")
subject = os.environ.get("INPUT_SUBJECT")
body = os.environ.get("INPUT_BODY")
sender_email = os.environ.get("INPUT_FROM")
ssl_tls = os.environ.get("INPUT_SSL")

def set_output(name, value):
    with open(os.environ['GITHUB_OUTPUT'], 'a') as f:
        print(f'{name}={value}', file=f)
        
def validate_mail(email):
    # pass the regula expression
    # and the string into a fullmathc method
    try:
        re.fullmatch(regex, email)
        return true
    except:
        value = email + " {0}"
        set_output("status",value.format("is not valid") )
        return false
def send_email():
    # Check if any of the environment variables are empty or None
    if None in (smtp_port, smtp_address, sender_email_auth, sender_password_auth, receiver_email, sender_email) or '' in (smtp_port, smtp_address, sender_email_auth, sender_password_auth, receiver_email, sender_email):
             # writing to the buffer
            output = "One or more required environment variables are empty or not set."
            #io.write_to_output({"status": f"Error: {output}"})
            set_output("status", "environment variables are empty or None")
            raise ValueError(output)
        
    message = MIMEMultipart("alternative")
    message["Subject"] = subject
    message["From"] = sender_email
    text = body
    part1 = MIMEText(text, "plain")
    message.attach(part1)
    
    if (len(receiver_email.split(",")) >= 1):
        emails = receiver_email.split(",")
        for email_addr in emails:
            if(email_addr.strip()):
                message["To"] = email_addr.strip()
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
                server.sendmail(sender_email, email_addr, message.as_string())
                except Exception as e:
                    output = "One or more required environment variables are empty or not set."
                    set_output("status", output)
                    print(e)
                finally:
                server.quit()
    else:
        set_output("status", "error: set at least one email")
        raise Exception("at least one valid  receiver email is expected")

if __name__ == "__main__":
    send_email()
