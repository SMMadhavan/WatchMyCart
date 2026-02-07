import smtplib
from email.mime.text import MIMEText

# Mail Alert
def send_email_alert(to_email, product, current, target):
    from_email = "abc_@gmail.com"
    app_password = "xyz"

    subject = "WatchMyCart Alert!"
    body = f"""
Price Alert Triggered!

Product: {product}
Current Price: {current}
Target Price: {target}

Time to buy.
"""

    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = from_email
    msg["To"] = to_email

    server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
    server.login(from_email, app_password)
    server.send_message(msg)
    server.quit()
