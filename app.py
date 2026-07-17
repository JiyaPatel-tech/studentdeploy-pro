from flask import Flask
import json

app = Flask(__name__)

@app.route("/")
def home():
    with open("students.json", "r") as file:
        students = json.load(file)

    topper = max(students, key=lambda x: x["marks"])

    return f"""
    <html>
    <head>
        <title>Student Deploy Demo</title>
    </head>
    <body style="font-family:Arial;text-align:center;margin-top:100px;">
        <h1>Student Deployment Demo</h1>
        <h2>Topper: {topper['name']}</h2>
        <h3>Marks: {topper['marks']}</h3>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)