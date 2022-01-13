import smtplib
from email.mime.text import MIMEText
from email.header import Header


def sendEmail(textMsg):
    sender = "aetheryneAuto@gmail.com"
    password = "dnb3s3mk"

    receiver = ["zifa25796@outlook.com"]

    mail_server = "smtp.gmail.com"

    msg = MIMEText(textMsg, "plain", "utf-8")
    msg["Subject"] = Header(u"Stock update", "utf-8").encode()

    try:
        server = smtplib.SMTP(mail_server, 587)
        server.ehlo()
        server.starttls()
        server.login(sender, password)
        server.sendmail(sender, receiver, msg.as_string())
        server.close()
        print("Sent")
    except smtplib.SMTPException as e:
        print("Failed")
        print(e)
