
# Exercise 2: Deploy a Flask App on Minikube

## Objective
To build and deploy a Python Flask web application on Kubernetes using Minikube, a Docker image, Kubernetes Deployment, and Service YAML files.

## Technologies Used
- Python
- Flask
- Docker image
- Kubernetes
- Minikube
- kubectl

## Project Files
- `app.py` — Flask web application
- `Dockerfile` — Instructions to build the application image
- `deployment.yaml` — Kubernetes Deployment configuration
- `service.yaml` — Kubernetes NodePort Service configuration

## Implementation
1. Created a Flask application that returns a greeting.
2. Created a Dockerfile to package the Flask application.
3. Built the image `flask-minikube:v1` inside Minikube.
4. Created a Kubernetes Deployment to run one replica.
5. Created a NodePort Service to expose the application on port 30080.
6. Applied the YAML files using `kubectl`.
7. Verified that the Deployment was ready and the Pod was running.
8. Opened the application in a browser and confirmed the response.

## Expected Output
`Hello from Flask on Kubernetes!`

## Conclusion
The Flask application was successfully deployed on Minikube using Kubernetes YAML configurations. The application was verified in a browser through the Kubernetes Service.
