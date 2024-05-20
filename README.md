This is the emailing mircroservice that welcome new user when they sign up successfully.

In order to use this microservice in your program. Follow these steps:

***Step 1: Create an account for your program to send the welcome email.***
  + Create a new account on gmail.com
  + Enable 2-factor authentication for your account
  + Go to https://myaccount.google.com/u/3/apppasswords to retrieve an app password for the microservice
  + Save that in your local computer
    
***Step 2: Setting up***
  + In your file, replace 2 constants at the top of api.py
  + EMAIL_ADDRESS will be your email address used to send the welcome emails
  + EMAIL_PASSWORD will be the app password that you just created above
  + In your terminal, enter "pip install flask" if you haven't installed it yet.

***Step 3: Communicate with the Microservice***
  + Run the microservice with this command "python3 api.py"
  + To communicate with the microservice, send an API request to 
