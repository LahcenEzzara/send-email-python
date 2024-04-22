# Import necessary libraries
from dotenv import load_dotenv
import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Load environment variables from a .env file
load_dotenv()

# Retrieve environment variables
HOST = os.getenv("HOST")
PORT = int(os.getenv("PORT"))
SENDER_EMAIL = os.getenv("SENDER_EMAIL")
RECEIVER_EMAIL = os.getenv("RECEIVER_EMAIL")
PASSWORD = os.getenv("PASSWORD")

# Create a multipart message and set headers
message = MIMEMultipart("alternative")
message['Subject'] = "Greetings from Lahcen"
message['From'] = SENDER_EMAIL
message['To'] = RECEIVER_EMAIL

# Read the HTML file
with open("index.html", "r") as file:
    html = file.read()

# Convert HTML file to MIMEText objects
html_part = MIMEText(html, 'html')

# Add HTML part to MIMEMultipart message
# The email client will try to render the last part first
message.attach(html_part)

# Create secure connection with server and send email
try:
    smtp = smtplib.SMTP(HOST, PORT)
    smtp.starttls()
    smtp.login(SENDER_EMAIL, PASSWORD)
    smtp.sendmail(SENDER_EMAIL, RECEIVER_EMAIL, message.as_string())
    print("Email sent successfully!")
except Exception as e:
    print(f"Failed to send email: {e}")
finally:
    smtp.quit()
