This is the emailing mircroservice that welcome new user when they sign up successfully.

In order to use this microservice in your program. Follow these steps:

***Step 1: Send a GET request to the microservice server.***
  + The microservice server is located at https://dekkov.pythonanywhere.com/
  + This is an example of the GET request: https://dekkov.pythonanywhere.com/send-email/"tranhoan@oregonstate.edu"?user_name=Hoang
  + The user_name part is optional but you have to specify the specific request send-email along with the new user's email address.

    
***Step 2: Get JSON File***
  + After sending the request, you will receive a JSON object that indicates if the email has been successfully sent.
  + Example of JSON response
  ![image](https://github.com/dekkov/microservice/assets/99220799/f69062f9-6b46-4f39-80e4-fc46ab7d5c24)


***UML Sequence Diagram***

![Screenshot 2024-05-20 at 12 54 44 PM](https://github.com/dekkov/microservice/assets/99220799/6ff02922-ee44-4ed3-8f4b-7c089f6bb354)
