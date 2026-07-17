# Scalable Python Web Application using Docker, Amazon ECR and Amazon ECS

## Project Overview

This project demonstrates the deployment of a containerized Python web application using Docker and Amazon Web Services (AWS). The application is developed using Flask, packaged into a Docker container, stored in Amazon Elastic Container Registry (ECR), and deployed using Amazon Elastic Container Service (ECS) with AWS Fargate.

The project showcases a modern container-based deployment workflow commonly used in cloud-native application development.

---

## Features

- Python Flask web application
- Docker containerization
- Amazon Elastic Container Registry (ECR) integration
- Amazon Elastic Container Service (ECS) deployment
- AWS Fargate serverless compute
- Health check endpoint
- CloudWatch log integration

---

## Technologies Used

- Python 3
- Flask
- Docker
- Amazon ECS
- Amazon ECR
- AWS Fargate
- Amazon CloudWatch
- IAM

---

## Project Structure

```
studentdeploy-pro/
│
├── .github/
│   └── workflows/
│       └── deploy.yml
│
├── screenshots/
│   ├── AmazonECR.png
│   ├── AmazonECS.png
│   ├── EC2-Instance.png
│   ├── ecs-service.png
│   ├── ecs-task-fargate.png
│   └── task-definition.png
│
├── app.py
├── deploy.py
├── requirements.txt
├── students.json
├── .gitignore
└── README.md
```

---

## Application Endpoints

| Endpoint | Description |
|----------|-------------|
| `/` | Returns the application welcome message |
| `/health` | Returns the application health status |

---

## Docker Commands

### Build Docker Image

```bash
docker build -t ecs-python-app .
```

### Run Docker Container

```bash
docker run -d -p 5000:5000 ecs-python-app
```

### List Running Containers

```bash
docker ps
```

---

## Deployment Workflow

1. Develop the Flask application.
2. Create a Docker image.
3. Push the Docker image to Amazon ECR.
4. Create an Amazon ECS Cluster.
5. Configure an ECS Task Definition.
6. Deploy the application using AWS Fargate.
7. Verify the running ECS service.

---

## AWS Services Used

- Amazon Elastic Container Registry (ECR)
- Amazon Elastic Container Service (ECS)
- AWS Fargate
- Amazon CloudWatch
- AWS Identity and Access Management (IAM)

---

## Deployment Screenshots

The `screenshots` directory contains deployment screenshots demonstrating:

- Amazon ECR Repository
- Amazon ECS Cluster
- ECS Service
- ECS Task running on AWS Fargate
- ECS Task Definition
- EC2 Instance (if used during the deployment workflow)

---

## Learning Outcomes

This project demonstrates practical experience with:

- Containerizing Python applications using Docker
- Managing Docker images in Amazon ECR
- Deploying containers using Amazon ECS
- Running serverless containers with AWS Fargate
- Configuring ECS task definitions and services
- Understanding cloud-native application deployment

---

## Author

**Jiya Patel**

Computer Science Student

GitHub: https://github.com/JiyaPatel-tech