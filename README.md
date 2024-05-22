This is the emailing mircroservice that welcome new user when they sign up successfully.

In order to use this microservice in your program. Follow these 2 parts:

***Part 1: Send a request to the microservice server.***
  + The microservice server is located at https://dekkov.pythonanywhere.com/
  + This is an example of the request: https://dekkov.pythonanywhere.com/send-email/"tranhoan@oregonstate.edu"?user_name=Hoang
  + Example of requesting <img width="604" alt="image" src="https://github.com/dekkov/microservice/assets/99220799/f3a50212-3a0b-48a1-9a87-26477da330cc">

  + The user_name part is optional but you have to specify the specific request send-email along with the new user's email address.

    
***Part 2: Receive JSON Response***
  + After sending the request, you will receive a JSON object that indicates if the email has been successfully sent.
  + Example of JSON response
  ![image](https://github.com/dekkov/microservice/assets/99220799/f69062f9-6b46-4f39-80e4-fc46ab7d5c24)
  + Example of Getting response:
    <img width="611" alt="image" src="https://github.com/dekkov/microservice/assets/99220799/49685651-1cea-4f3b-8002-785d5c73faeb">



***UML Sequence Diagram***

![Screenshot 2024-05-20 at 12 54 44 PM](https://github.com/dekkov/microservice/assets/99220799/6ff02922-ee44-4ed3-8f4b-7c089f6bb354)
