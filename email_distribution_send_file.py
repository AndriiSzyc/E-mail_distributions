from configs import password, users, sender

import smtplib, ssl
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

all_users = ", ".join(users)

# Create a multipart message and set headers
message = MIMEMultipart()
message["Subject"] = "Lecture 2 about Emails"
message["From"] = sender
message["To"] = all_users

# Add body to email
lecture_text = MIMEText("Hello, there! \nPlease take a look at this lecture!", "plain")
message.attach(lecture_text)

filename = "some_PDF_file.pdf"  # In same directory as script

# Open PDF file in binary mode
with open(filename, "rb") as attachment:
    # Add file as application/octet-stream
    # Email client can usually download this automatically as attachment
    part = MIMEBase("application/pdf", "octet-stream")
    part.set_payload(attachment.read())

# Encode file in ASCII characters to send by email
encoders.encode_base64(part)

# Add header as key/value pair to attachment part
part.add_header("Content-Disposition", f"attachment; filename={filename}")

# Add attachment to message and convert message to string
message.attach(part)
text = message.as_string()

# Log in to server using secure context and send email
context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(user=sender, password=password)
    server.ehlo()
    server.sendmail(sender, users, text)
