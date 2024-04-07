from flask_login import current_user
import json
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from dotenv import load_dotenv
import os
from app.models.Location import Location
from email.mime.base import MIMEBase
from email import encoders

load_dotenv()

def load_emails():
    with open('app/data/user_settings.json', 'r', encoding='utf-8') as settings:
        data = json.load(settings)
    
    to = data['to']
    
        
    if data['send-to'] == 'location':
        locations = data['filters']
        companies = []
        for location in locations:
            all_companies = Location.get_all_companies_by_location(to, location[f'{to}_name'])
            if len(all_companies) < 1: 
                continue
            
            for company in all_companies:
                companies.append(company)

    elif data['send-to'] == 'all':
        with open('app/data/companies.json', 'r', encoding='utf-8') as companies:
            companies = json.load(companies)['companies']

    emails = [company['company_email_address'] for company in companies]
    return emails


def send_email(addressee='all'): 
    
    # emails = load_emails()
    emails = ['cfmorales.diaz20@gmail.com']
    
    if (addressee == 'user'):
        emails = [current_user.email_address]
    
    if len(emails) < 1:
        return {
            "status": False,
            "message": "No emails found for that location"
        }
    
    
    
    smtp_host = os.getenv('SMTP_HOST')
    smtp_port = os.getenv('SMTP_PORT')
    email_usuario = current_user.email_address
    email_password = current_user.google_password
    subject = current_user.mail.mail_subject
    mail_content = current_user.mail.mail_content
    msg = MIMEMultipart()
    

    
    msg['From'] = email_usuario
    msg["Bcc"] = ", ".join(emails)
    msg['Subject'] = subject
    msg.attach(MIMEText(mail_content, 'plain'))
    
    with open(f"app/static/files/{current_user.mail.mail_file}", "rb") as adjunto:
        parte_adjunta = MIMEBase("application", "octet-stream")
        parte_adjunta.set_payload(adjunto.read())
        encoders.encode_base64(parte_adjunta)
        parte_adjunta.add_header(
            "Content-Disposition", f"attachment; filename= {current_user.mail.mail_file}"
        )
        msg.attach(parte_adjunta)
    
    try:
        with smtplib.SMTP(smtp_host, smtp_port) as servidor_smtp:
            servidor_smtp.starttls()
            servidor_smtp.login(email_usuario, email_password)
            servidor_smtp.send_message(msg)
            return {"status": True}
    except Exception as ex:
        print(ex)
        return {"status": False}