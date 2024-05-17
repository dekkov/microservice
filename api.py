from flask import Flask, request, jsonify
import os
import smtplib
from email.message import EmailMessage

EMAIL_ADDRESS = 'cs361tranhoan'
EMAIL_PASSWORD = 'edis cihs qhzr oqen'

def send_email(t,subject = "Welcome Email", username="New User"):
    msg = EmailMessage()

    body = f"Hello, {username}.\n We welcome you onboard! Hope you will have a good time!"

    msg['Subject'] = subject
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = t
    msg.set_content(body)


    with smtplib.SMTP('smtp.gmail.com', 587) as smtp: 
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()

        smtp.login(EMAIL_ADDRESS,EMAIL_PASSWORD)


        smtp.send_message(msg)

app = Flask(__name__)

@app.route("/send-email/<user_email>")
def get_user(user_email):
    user_name = request.args.get("user_name")
    if user_name:
        send_email(t=user_email,username=user_name)
    else:
        send_email(user_email)
    
    user_data = {
        "user_email": user_email,
        "State": "Successful",
    }

    return jsonify(user_data), 200

if __name__ == "__main__":
    app.run(debug=True)