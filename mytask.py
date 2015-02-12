'''
Created on Feb 12, 2015

@author: vivek
'''
from email.mime.text import MIMEText
import smtplib
from mycelery import celery

@celery.task
def add(a,b):
    c = a+b
    print "addition is  = " + str(c) 

@celery.task
def send_email(to=None, subject=None, message=None):
    """sends email from hairycode-noreply to specified destination

    :param to: string destination address
    :param subject: subject of email
    :param message: body of message

    :return: True if successful
    """
    # prep message
    fro="hairycode-noreply@hairycode.org"
    msg = MIMEText(message)
    msg['Subject'] = subject
    msg['From'] = fro 
    msg['To'] = to

    # send message
    s = smtplib.SMTP('mail.hairycode.org')
    s.ehlo()
    s.starttls()
    s.ehlo()
    s.login('YOUR_USERNAME', 'YOUR_PASSWORD')
    #s.sendmail('hairycode-noreply@hairycode.org, [to], msg.as_string())
    s.quit()
    return True