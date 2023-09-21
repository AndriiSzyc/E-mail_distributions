from configs import password, users, sender
import smtplib
import ssl


title_message = "Python mini course!"
body_message = "Hi there,\n How are you?"
message = f"Subject: {title_message}\n\n{body_message}"

# Create a secure SSL context
context = ssl.create_default_context()

with smtplib.SMTP_SSL(
    host="smtp.gmail.com", port=465, context=context
) as server:  # creating a secure connection to the server
    server.login(user=sender, password=password)
    server.ehlo()
    for user in users:
        server.sendmail(sender, user, message)

# Second option
# # Try to log in to server and send email
# try:
#     server = smtplib.SMTP_SSL(host='smtp.gmail.com', port=465, context=context)
#     server.login(user=sender, password=password)
#     server.ehlo()
#     for user in users:
#         server.sendmail(sender, user, msg=message)
# except Exception as e:
#     print(e)
#     # Print any error messages to stdout
# finally:
#     server.quit()
