from configs import password, users, sender


def send_email(user, pwd, recipient, subject, body):
    # user - sender, pwd - password, recipient - users, subject - e-mail_titl, body - e-mail_message
    import smtplib
    import ssl

    context = ssl.create_default_context()

    FROM = user
    TO = recipient if isinstance(recipient, list) else [recipient]
    SUBJECT = subject
    TEXT = body

    # Prepare actual message
    message = """From: %s\nTo: %s\nSubject: %s\n\n%s
    """ % (
        FROM,
        ", ".join(TO),
        SUBJECT,
        TEXT,
    )
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls(context=context)
        server.login(user, pwd)
        server.sendmail(user, TO, message)
        print("successfully sent the mail")
    except Exception as e:
        print(e)
        print("failed to send mail")
    finally:
        server.close()


"""Calling func"""

title_message = "Python mini course!"
body_message = "Hi there,\nHow are you?"

send_email(sender, password, users, title_message, body_message)
