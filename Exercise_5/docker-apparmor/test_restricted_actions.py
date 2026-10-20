
import docker

client = docker.from_env()

try:
    container = client.containers.run(
        "flask-apparmor",
        command="python -c \"import time; time.sleep(60)\"",
        security_opt=["apparmor=my-apparmor-profile"],
        detach=True
    )

    # Test access to a protected file
    result = container.exec_run("cat /etc/passwd")
    print("Test 1: Read /etc/passwd")
    print("Exit code:", result.exit_code)
    print(result.output.decode(errors="replace"))

    # Test execution of a shell
    result = container.exec_run("/bin/sh -c 'echo Shell executed'")
    print("Test 2: Execute shell")
    print("Exit code:", result.exit_code)
    print(result.output.decode(errors="replace"))

except docker.errors.APIError as error:
    print("Docker could not start the container with the requested profile.")
    print("This may happen because custom AppArmor profiles are not supported")
    print("by the current Docker Desktop environment.")
    print("Details:", error)

finally:
    try:
        container.stop()
        container.remove()
    except (NameError, docker.errors.APIError):
        pass
