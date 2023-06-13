from flask import Flask    

app = Flask(__name__)   #initialize app within application running on Flask (define the URL for the application)

from application import routes

if __name__ == '__main__':
    app.run()
    