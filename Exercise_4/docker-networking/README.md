\# Exercise 4: Docker Networking with Multiple Containers



\## Objective

To understand Docker bridge networking and configure communication between multiple containers.



\## Technologies Used

\- Docker

\- Python

\- Flask

\- MySQL

\- Redis



\## Project Structure

```text

docker-networking/

├── app.py

├── requirements.txt

├── Dockerfile

└── README.md

```



\## Step 1: Create a Custom Bridge Network

```powershell

docker network create --driver bridge my-bridge-net

docker network ls

docker network inspect my-bridge-net

```



\## Step 2: Build the Flask Image

```powershell

docker build -t flask-api .

```



\## Step 3: Start the Containers

```powershell

docker run -d --name mysql --network my-bridge-net -e MYSQL\_ROOT\_PASSWORD=LabRoot123 mysql:latest

docker run -d --name redis --network my-bridge-net redis:latest

docker run -d --name flask --network my-bridge-net -p 5001:5001 flask-api

```



\## Step 4: Test the Application

Open the following URL in a browser:



`http://localhost:5001/about`



Expected response:

```json

{

&#x20; "name": "Simple REST API",

&#x20; "version": "1.0",

&#x20; "description": "This is a simple REST API built with Flask."

}

```



\## Step 5: Test Container Connectivity

Enter the Flask container:

```bash

docker exec -it flask bash

```



Test MySQL:

```bash

ping -c 4 mysql

```



Test Redis:

```bash

ping -c 4 redis

```



Both tests succeeded with four packets received and zero packet loss.



\## Step 6: Docker Network Inspection

```powershell

docker network inspect my-bridge-net

```



The custom bridge network connects the Flask, MySQL, and Redis containers. Containers can discover one another using container names.



\## Questions and Answers



\### 1. What is the purpose of the `--net` or `--network` flag?

It specifies the Docker network to which a container should connect.



\### 2. How can containers on the same network communicate?

They can communicate using container names or IP addresses. Docker provides name resolution on a user-defined bridge network.



\### 3. What is the difference between bridge and host networking?

\- \*\*Bridge:\*\* Containers communicate through an isolated virtual network.

\- \*\*Host:\*\* A container shares the host's network stack.



\### 4. How can a container port be exposed to the host?

Use the `-p` option. For example, `-p 5001:5001` maps host port 5001 to container port 5001.



\## Result

Successfully created a custom Docker bridge network and ran Flask, MySQL, and Redis containers on it. Verified Flask API access and confirmed connectivity from Flask to MySQL and Redis using ping.



