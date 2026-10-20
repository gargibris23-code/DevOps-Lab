# Exercise 3: Flash Sale App on Kubernetes

## Objective
To deploy a Flask-based Flash Sale application on a single-node Kubernetes cluster using a ReplicaSet and Service.

## Technologies Used
- Python and Flask
- Docker
- Kubernetes
- Minikube
- PowerShell

## Application Features
- **Homepage (`/`)**: Displays a welcome message and the Pod hostname.
- **Buy (`/buy`)**: Returns a randomly selected product and user information.
- **Health Check (`/health`)**: Reports the application health status.

## Kubernetes Components
- **ReplicaSet:** Maintains the desired number of application Pods.
- **Service:** Exposes the application internally and distributes requests across eligible Pods.
- **Readiness Probe:** Checks whether a Pod is ready to receive traffic.
- **Liveness Probe:** Checks whether the application is healthy.

## Implementation
1. Created the Flask application in `app.py`.
2. Created a Dockerfile to package the application.
3. Built the image `flashsale:1.0` using Minikube.
4. Created `flashsale-replicaset.yaml` containing the ReplicaSet and Service definitions.
5. Deployed the resources using `kubectl apply`.
6. Scaled the ReplicaSet from 3 to 5 Pods.
7. Deleted a Pod and verified that Kubernetes automatically created a replacement.
8. Tested the application endpoints using port forwarding.

## Commands Used
```powershell
minikube image build -t flashsale:1.0 .
kubectl apply -f flashsale-replicaset.yaml
kubectl get pods
kubectl get rs flashsale-rs
kubectl scale rs flashsale-rs --replicas=5
kubectl delete pod <pod-name>
kubectl get service flashsale-svc
kubectl port-forward service/flashsale-svc 8080:80
```

## Result
The Flash Sale application was successfully deployed on a single-node Minikube cluster. All five ReplicaSet Pods were running and ready. Kubernetes automatically replaced a deleted Pod, and the application endpoints were verified successfully.

## Conclusion
This exercise demonstrates Kubernetes ReplicaSet management, scaling, self-healing, health checks, and Service-based access to a containerized Flask application.
