from flask import Flask
import os


app=Flask(__name__)

@app.route('/',methods=['GET'])
def index():
    return "hello world1"



if __name__=="__main__":
    app.run()