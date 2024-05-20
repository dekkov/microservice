from flask import Flask, request, jsonify
import os
import smtplib
from email.message import EmailMessage

EMAIL_ADDRESS = 'cs361tranhoan'
EMAIL_PASSWORD = 'edis cihs qhzr oqen'

SMTP_ERROR_CODES = {
    211: "System status, or system help reply.",
    214: "Help message.",
    220: "Service ready.",
    221: "Service closing transmission channel.",
    235: "Authentication successful.",
    250: "Requested mail action okay, completed.",
    251: "User not local; will forward to {}",
    252: "Cannot VRFY user, but will accept message and attempt delivery.",
    354: "Start mail input; end with <CRLF>.<CRLF>",
    421: "Service not available, closing transmission channel. The server response was: {}",
    450: "Requested mail action not taken: mailbox unavailable. The server response was: {}",
    451: "Requested action aborted: local error in processing.",
    452: "Requested action not taken: insufficient system storage.",
    455: "Server unable to accommodate parameters.",
    500: "Syntax error, command unrecognized.",
    501: "Syntax error in parameters or arguments.",
    502: "Command not implemented.",
    503: "Bad sequence of commands.",
    504: "Command parameter not implemented.",
    530: "Authentication required.",
    534: "Authentication mechanism is too weak.",
    535: "Authentication failed. The server response was: {}",
    538: "Encryption required for requested authentication mechanism.",
    550: "Requested action not taken: mailbox unavailable. The server response was: {}",
    551: "User not local; please try {}. The server response was: {}",
    552: "Requested mail action aborted: exceeded storage allocation.",
    553: "Requested action not taken: mailbox name not allowed.",
    554: "Transaction failed. The server response was: {}",
}

def send_email(t,subject = "Welcome Email", username="New User"):
    msg = EmailMessage()

    body = f"Hello, {username}.\n We welcome you onboard! Hope you will have a good time!"

    msg['Subject'] = subject
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = t
    msg.set_content(body)


    with smtplib.SMTP('smtp.gmail.com', 587) as smtp: 
        try:
            smtp.ehlo()
            smtp.starttls()
            smtp.ehlo()

            smtp.login(EMAIL_ADDRESS,EMAIL_PASSWORD)


            smtp.send_message(msg)

            response = {
                "user_email": t,
                "State": "Queued. Thank you!",
            }

            return response
        except smtplib.SMTPResponseException as err:
            
            error_code = err.smtp_code
            error_message = SMTP_ERROR_CODES.get(error_code, f"Unknown error ({error_code})")
            response = {
                "Error code": error_code,
                "Error message": error_message,
            }


            return response
        
        except Exception as Err:
            response = {
                "Error message": f"Error sending email to {t}",
            }

            return response

app = Flask(__name__)

@app.route("/send-email/<user_email>")
def get_user(user_email):
    user_name = request.args.get("user_name")
    if user_name:
        response = send_email(t=user_email,username=user_name)
    else:
        response = send_email(user_email)
    

    return jsonify(response), 200

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080,debug=True)