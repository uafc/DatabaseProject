# Project Setup Instructions

## 1. Configure environment variable

1. After cloning the repository, navigate to your local repository folder.
2. Create a `.env` file to store your OMDB API key. This file will be used to store your OMDB API Key, which the python program will extract and use.

   In your `.env` file, add the following line:

   ```plaintext
   OMDB_API_KEY=api_key
 
- Make sure api_key is your actual api_key, with no quotation marks
  
## 2. Configure virtual environment to run this program
To run this program:
1. First ensure that you have virtualenv installed: https://virtualenv.pypa.io/en/latest/installation.html#via-pip
2. Then, create a virtual environment by typing into your terminal: virtualenv -p python3 .venv
3. Then, activate your virtual environment by doing: source .venv/bin/activate
4. Once you have activated your virtual environment, type into your terminal: pip install -r requirements.txt. This will install the required python packages inside of your virtual environment
5. Once you have finished working in your virtual environment, type "deactivate" in terminal to deactivate your virtual environment.


## 3. Running this program on replit
This code will function the same on replit, the only difference is that you need to store the API key in the "Replit Secrets" section of your repl. So, we will NOT be creating a .env file in our repl, and we will NOT be installing and importing the python-dotenv/dotenv module.
