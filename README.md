🚀 Kubernetes Microservices Application

A simple frontend–backend microservices application deployed on Kubernetes using Docker containers, Kubernetes Deployments, Services, and Ingress.
This project demonstrates containerization, service discovery, and Kubernetes orchestration.

📌 Project Overview

Frontend: Static HTML application

Backend: Python Flask REST API

Containerized using Docker

Deployed on Kubernetes

Frontend communicates with backend using Kubernetes Service

🏗️ Project Structure
k8s-microservice/
│
├── backend/
│   ├── app.py
│   ├── requirements.txt
│   └── Dockerfile
│
├── frontend/
│   ├── index.html
│   └── Dockerfile
│
├── k8s/
│   ├── backend-deployment.yaml
│   ├── backend-service.yaml
│   ├── frontend-deployment.yaml
│   ├── frontend-service.yaml
│   └── ingress.yaml
│
└── README.md

⚙️ Technologies Used

Docker

Kubernetes

Python (Flask)

HTML

Git & GitHub

Docker Hub

