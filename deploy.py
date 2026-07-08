import subprocess

print("Starting Deployment...")

subprocess.run(["python", "app.py"], check=True)

print("Deployment Successful")