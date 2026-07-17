# Student Deployment Demo

## Project Overview

Student Deployment Demo is a simple Flask-based web application that demonstrates deploying a Python application on a Linux server. The application reads student information from a JSON file, identifies the topper based on marks, and displays the result through a web interface.

This project focuses on learning application deployment using Python and Flask.

---

## Features

- Reads student records from a JSON file
- Finds the student with the highest marks
- Displays topper information
- Simple HTML interface
- Flask web server
- Python deployment script

---

## Technologies Used

- Python
- Flask
- JSON
- HTML
- Linux
- Git
- GitHub

---

## Project Structure

```
studentdeploy-pro/
│
├── app.py
├── deploy.py
├── students.json
├── requirements.txt
├── README.md
└── screenshots/
```

---

## How It Works

1. Flask starts the application.
2. Student records are loaded from `students.json`.
3. The application identifies the student with the highest marks.
4. The topper's details are displayed on the homepage.

---

## Running the Project

Install dependencies:

```bash
pip install -r requirements.txt
```

Start the application:

```bash
python deploy.py
```

or

```bash
python app.py
```

Open:

```
http://localhost:5000
```

---

## Screenshots

The `screenshots` folder contains:

- Application Homepage
- Flask Running
- Deployment Process
- EC2 Deployment (if applicable)

---

## Learning Outcomes

- Flask web development
- Reading JSON data
- Python scripting
- Web application deployment
- Git and GitHub workflow

---

## Author

**Jiya Patel**

Computer Science Student

GitHub: https://github.com/JiyaPatel-tech