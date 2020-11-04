import smtplib
from email.message import EmailMessage

# Email alert python script from ©elOreo: https://github.com/elOreo
def email_alert(subject, body, to):
    msg = EmailMessage()
    msg.set_content(body)
    msg['subject'] = subject
    msg['to'] = to

    user = "from@domain.com"
    msg['from'] = user

    # Set the password to the Password your eMail provider provides you for 3rd Party Apps. (You might have to set this up first)
    password = "password"

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(user, password)
    server.send_message(msg)

    server.quit()


if __name__ == '__main__':

    email_alert("subject", "body", "to@domain.com")

