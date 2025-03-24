import smtplib
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

# Email credentials (use environment variables for security)
EMAIL_ADDRESS = "Enter your email address"
EMAIL_PASSWORD = "Enter app password"  # Use an App Password if needed
SMTP_SERVER = "smtp.gmail.com"  # Change if using another email provider
SMTP_PORT = 587  # Standard for TLS

# File paths
EMAIL_LIST_FILE = "recruiter_emails.txt"  # Text file containing recruiter emails (one per line)
RESUME_PATH = "Path"  # Path to your resume

# Email content
SUBJECT = "Reaching out for opportunities"
EMAIL_BODY = """\
Hello {name},

Enter your email body
"""

def send_email(recipient_email, recipient_name):
    msg = MIMEMultipart()
    msg["From"] = EMAIL_ADDRESS
    msg["To"] = recipient_email
    msg["Subject"] = SUBJECT

    # Personalize email body
    email_body = EMAIL_BODY.format(name=recipient_name)
    msg.attach(MIMEText(email_body, "plain"))

    # Attach resume
    with open(RESUME_PATH, "rb") as attachment:
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())
        encoders.encode_base64(part)
        part.add_header("Content-Disposition", f"attachment; filename={os.path.basename(RESUME_PATH)}")
        msg.attach(part)

    # Send email
    try:
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        server.sendmail(EMAIL_ADDRESS, recipient_email, msg.as_string())
        server.quit()
        print(f"Email sent to {recipient_name} at {recipient_email}")
    except Exception as e:
        print(f"Failed to send email to {recipient_email}: {e}")
 
def main():
    with open(EMAIL_LIST_FILE, "r") as file:
        for line in file:
            line = line.strip()
            if line:
                parts = line.split(",")  # Split email and name
                if len(parts) == 2:
                    email, name = parts[0].strip(), parts[1].strip()
                    send_email(email, name)
                else:
                    print(f"Skipping invalid line: {line}")

if __name__ == "__main__":
    main()
