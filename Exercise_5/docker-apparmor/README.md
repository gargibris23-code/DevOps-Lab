\# Exercise 5: Docker Security with AppArmor and Python



\## 1. Objective

To understand Docker container security using AppArmor and Python Docker SDK. This exercise demonstrates how security profiles can restrict container actions.



\## 2. Technologies Used

\- Python and Flask

\- Docker

\- Docker SDK for Python

\- AppArmor

\- Windows PowerShell and Docker Desktop



\## 3. Project Files

\- `app.py` – Flask application.

\- `Dockerfile` – builds the Flask Docker image.

\- `my-apparmor-profile` – starter AppArmor security policy.

\- `apply\_apparmor.py` – requests the profile and inspects container security settings.

\- `test\_restricted\_actions.py` – tests file access and shell execution.

\- `requirements.txt` – lists Python dependencies.



\## 4. Flask Application

The Flask application displays a message when a user visits the home page.



Expected output:



`Hello, this is a secure Flask application running inside a Docker container!`



\## 5. Build and Run the Docker Image



Build the image:



```bash

docker build -t flask-apparmor .

```



Run the container:



```bash

docker run -d --name flask-apparmor-test -p 5000:5000 flask-apparmor

```



Open `http://localhost:5000/` in a browser to verify the application.



\## 6. AppArmor Security

AppArmor is a Linux security module that restricts what applications can access and execute. Docker can use AppArmor profiles to apply additional restrictions to containers.



A suitable profile can restrict:

\- Access to sensitive files.

\- Writing to protected system directories.

\- Execution of unauthorized programs.

\- Dangerous administrative capabilities.



The profile must be validated and tested on a compatible Linux host before its restrictions can be considered effective.



\## 7. Python Docker SDK

The Docker SDK allows Python programs to communicate with Docker, build images, start containers, and inspect container settings.



Install the SDK:



```bash

py -m pip install docker

```



Run the scripts:



```bash

py apply\_apparmor.py

py test\_restricted\_actions.py

```



These scripts request the custom profile. Successful enforcement depends on the host operating system and Docker configuration.



\## 8. Environment Limitation

This exercise was prepared and tested using Windows PowerShell and Docker Desktop. The Flask image built successfully and the application displayed the expected message in the browser.



The Docker security options reported:



`\["name=seccomp,profile=builtin","name=cgroupns"]`



AppArmor was not listed. Therefore, custom AppArmor enforcement could not be confirmed in this environment. The profile must be loaded and tested on a compatible Linux system with AppArmor enabled.



\## 9. Conclusion

The Flask application was successfully containerized and tested. The Python Docker SDK and AppArmor policy files were prepared to demonstrate container security. Actual AppArmor enforcement requires a supported Linux environment and verification of the applied policy.



