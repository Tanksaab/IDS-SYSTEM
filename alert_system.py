import smtplib
from email.mime.text import MIMEText

def send_alert(subject, message):
    msg = MIMEText(message)
    msg['Subject'] = subject
    msg['From'] = 'your_email@example.com'
    msg['To'] = 'admin_email@example.com'
    server = smtplib.SMTP('your_smtp_server')
    server.sendmail('your_email@example.com', 'admin_email@example.com', msg.as_string())
    server.quit()

def flag_suspicious_activities(anomalies):
    for anomaly in anomalies:
        subject = 'Suspicious Activity Detected'
        message = f'Packet {anomaly} has been flagged as suspicious.'
        send_alert(subject, message)