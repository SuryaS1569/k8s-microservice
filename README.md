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

🐳 Docker Images
Service	Image
Backend	suryeahhhh73/backend:latest
Frontend	suryeahhhh73/frontend:latest
🚀 Deployment Steps
1️⃣ Build & Push Docker Images
# Backend
docker build -t suryeahhhh73/backend:latest backend/
docker push suryeahhhh73/backend:latest

# Frontend
docker build -t suryeahhhh73/frontend:latest frontend/
docker push suryeahhhh73/frontend:latest

2️⃣ Deploy to Kubernetes
kubectl apply -f k8s/


Verify:

kubectl get pods
kubectl get svc
kubectl get ingress

🌐 Application Access

Frontend exposed using NodePort / Ingress

Backend exposed using ClusterIP

Frontend communicates with backend via:

http://backend-service:8080

🔍 Service Communication Test
kubectl exec -it deployment/frontend-deployment -- curl http://backend-service:8080


Expected output:

Hello from Backend!