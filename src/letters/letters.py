import smtplib
from email.message import EmailMessage

from celery import Celery

from config import SMTP_HOST, SMTP_PORT, SMTP_USER, SMTP_PASS

celery = Celery('letters')

def send_email_template():
    email = "supermanformedia@gmail.com"
    with smtplib.SMTP_SSL(SMTP_HOST, SMTP_PORT) as server:
        server.login(SMTP_USER, SMTP_PASS)
        server.send_message(email)