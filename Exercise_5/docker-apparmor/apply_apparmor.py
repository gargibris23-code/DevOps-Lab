
import docker

client = docker.from_env()

# Build the Docker image
client.images.build(path=".", tag="flask-apparmor")
print("Docker image built successfully.")

# Start the container with the AppArmor profile
container = client.containers.run(
    "flask-apparmor",
    ports={"5000/tcp": 5000},
    security_opt=["apparmor=my-apparmor-profile"],
    detach=True
)

print(f"Container started: {container.short_id}")

# Inspect the container security settings
container_info = client.api.inspect_container(container.id)
security_options = container_info["HostConfig"]["SecurityOpt"]

print("Configured security options:", security_options)

container.stop()
container.remove()
print("Container stopped and removed.")
