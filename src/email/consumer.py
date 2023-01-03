from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib
from email_pb2 import SendReq, SendRes
from email_grpc import EmailsBase

import grpc
import os
#  Python grpc server to send emails


class Emails(EmailsBase):
    async def SendEmail(self, request, context):
        print("Sending email to: " + request.to)
        msg = MIMEMultipart()
        msg['From'] = os.environ.get("EMAIL_FROM", "ayuved009@gmail.com")
        msg['To'] = request.to
        msg['Subject'] = request.subject
        body = request.body
        msg.attach(MIMEText(body, 'plain'))
        server = smtplib.SMTP(os.environ.get(
            "EMAIL_SERVER", "smtp.gmail.com"),
            os.environ.get("EMAIL_PORT", 587)
        )
        server.starttls()
        server.login(os.environ.get("EMAIL_FROM", "ayuved009@gmail.com"),
                     os.environ.get("EMAIL_PASSWORD", "password"))
        text = msg.as_string()
        await server.sendmail(os.environ.get(
            "EMAIL_FROM", "sender@gmail.com"),
            request.to, text)
        server.quit()
        return SendRes(message="Email sent successfully")
