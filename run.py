# starting point of the app 
from app import create_app
from dotenv import load_dotenv

# load env variables
load_dotenv()

# create the app
app = create_app()

if __name__ == '__main__':
    app.run()
