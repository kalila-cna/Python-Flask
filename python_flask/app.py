
from flask import Flask

app=Flask(__name__)

@app.route('/',methods=['GET'])
def check():
    return "Hi KALILA ! This is the Task 3 of python flask assignment"


if __name__ == "__main__":
   app.run()