# Kubernetes Hello Pod — Zepto Storefront

## Objective
Deploy an Nginx container on a local Kubernetes cluster using Minikube and access it through a NodePort Service.

## Business Scenario
Zepto needs a lightweight storefront page that can run reliably in a containerized environment. In this exercise, Nginx simulates the storefront web application.

## Technologies Used
- Kubernetes
- Minikube
- kubectl
- Docker
- Nginx
- YAML
- Git and GitHub

## Prerequisites
Install Docker, Minikube, kubectl, and Git. Ensure Docker is running before starting the cluster.

## Implementation Steps

1. Start the local Kubernetes cluster:
   ```bash
   minikube start --driver=docker
   ```

2. Create the Pod:
   ```bash
   kubectl run hello-k8s --image=nginx --port=80
   ```

3. Verify the Pod:
   ```bash
   kubectl get pods
   ```

4. Expose the Pod:
   ```bash
   kubectl expose pod hello-k8s --type=NodePort --port=80
   ```

5. Verify the Service:
   ```bash
   kubectl get services
   ```

6. Open the application:
   ```bash
   minikube service hello-k8s
   ```

## Configuration-Based Deployment

The `k8s/` directory contains reusable Kubernetes manifests:

- `pod.yaml`: Defines the Nginx Pod.
- `service.yaml`: Exposes the Pod using a NodePort Service.

To deploy using these files, remove the resources created by the imperative commands first, then apply the manifests:

```bash
kubectl delete service hello-k8s
kubectl delete pod hello-k8s
kubectl apply -f k8s/pod.yaml
kubectl apply -f k8s/service.yaml
```

Verify the deployment:

```bash
kubectl get pods
kubectl get services
```

Access the application again:

```bash
minikube service hello-k8s
```

## Expected Result
The Pod reaches the Running state, the NodePort Service is created, and the Nginx welcome page is accessible through the browser.

## Conclusion
This exercise demonstrates how Kubernetes runs a containerized application as a Pod and exposes it using a Service. The YAML manifests make the configuration reusable and prepare the project for future enhancements, such as Deployments, replicas, and scaling.
