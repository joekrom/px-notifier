# Download base image bitnami
FROM bitnami/python:3.10-debian-12

# LABEL about the custom image
LABEL maintainer="joel.dfankam@yahoo.fr"
LABEL version="0.1"
LABEL description="This is a custom Docker Image for cloud foundry github action"
# Disable Prompt During Packages Installation
ARG DEBIAN_FRONTEND=noninteractive
# Update Ubuntu Software repository
RUN apt-get update && apt-get install -y
WORKDIR /app
COPY . /app
CMD ["python" "/app/notifier.py"]
