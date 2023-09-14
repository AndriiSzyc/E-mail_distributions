from configs import password, users, sender
import smtplib
import ssl


context = (
    ssl.create_default_context()
)  # contains mostly default values for SSL structures that are later created for connections.

title_message = "Python mini course!"
body_message = "Hi there,\n How are you?"
# message = f"Subject: {title_message}\n\n{body_message}"

message = """From: %s\nTo: %s\nSubject: %s\n\n%s
    """ % (
    sender,
    ", ".join(users),
    title_message,
    body_message,
)

with smtplib.SMTP(
    host="smtp.gmail.com", port=587
) as server:  # creating an insecure connection to the server
    server.ehlo()  # the meaning of the command is to present the client to the SMTP server.
    server.starttls(context=context)  # creating a secure connection to the server
    server.ehlo()
    server.login(user=sender, password=password)  # user login to the server
    for user in users:
        server.sendmail(
            from_addr=sender, to_addrs=user, msg=message
        )  # sending each user a message

# Second option

# try:
#     server = smtplib.SMTP(host='smtp.gmail.com', port=587)
#     server.ehlo()
#     server.starttls(context=context)
#     server.ehlo()
#     server.login(user=sender, password=password)

#     for user in users:
#         server.sendmail(from_addr=sender, to_addrs=user, msg=message)
# except Exception as e:
#     print(e)
# finally:
#     server.quit()
