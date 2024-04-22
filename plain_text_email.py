# Import necessary libraries
from dotenv import load_dotenv
import os
import smtplib
import ssl

# Load environment variables from a .env file
load_dotenv()

# Retrieve environment variables
HOST = os.getenv("HOST")
PORT = int(os.getenv("PORT"))
SENDER_EMAIL = os.getenv("SENDER_EMAIL")
RECEIVER_EMAIL = os.getenv("RECEIVER_EMAIL")
PASSWORD = os.getenv("PASSWORD")

# Define the email message
message = """\
Subject: Greetings from Lahcen

Hello,

I hope this message finds you well. This is an automated message sent from a Python script developed by Lahcen.

Best Regards,
Lahcen
"""

# Create a secure SSL context
context = ssl.create_default_context()

try:
    # Establish a connection with the SMTP server
    server = smtplib.SMTP(HOST, PORT)

    # Start TLS for security
    server.starttls(context=context)

    # Authenticate with the SMTP server
    server.login(SENDER_EMAIL, PASSWORD)

    # Send the email
    server.sendmail(SENDER_EMAIL, RECEIVER_EMAIL, message)

except Exception as e:
    # Print any error messages to stdout
    print(f"An error occurred: {e}")
finally:
    # Close the connection to the SMTP server
    server.quit()
