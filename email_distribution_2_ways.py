from configs import password, users, sender

import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

all_users = ", ".join(users)

message = MIMEMultipart("alternative")
message["Subject"] = "Multipart message"
message["From"] = sender
message["To"] = all_users

# Create the plain-text and HTML version of your message
text = """
Hi there, 
This is the first try of sending an email.
Please reach the www.google.com for more details.
"""

html_text = """
<html>
<body>
<p>Hi there,<br>
    Please reach the <a href="https://google.com">Google</a>
    for more details.
</p>
</body>
</html>
"""

# Turn these into plain/html MIMEText objects
part1 = MIMEText(text, "plain")
part2 = MIMEText(html_text, "html")

# Add HTML/plain-text parts to MIMEMultipart message
# The email client will try to render the last part first
message.attach(part1)
message.attach(part2)

# Create secure connection with server and send email
context = ssl.create_default_context()
with smtplib.SMTP_SSL(
    host="smtp.gmail.com", port=465, context=context
) as server:  # створення захищеного з'єднання з сервером
    server.login(user=sender, password=password)  # логування користувача до сервера
    server.ehlo()
    server.sendmail(sender, users, message.as_string())
