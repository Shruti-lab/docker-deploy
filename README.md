# Flask Tasks API - Dockerized Application

A simple REST API built with Flask for managing tasks, containerized with Docker.

Docker Image url: https://hub.docker.com/r/menu34iterate/flask-docker-app

## Features

- View all tasks
- Get task by ID
- Create new tasks
- Health check endpoint
- Fully containerized with Docker

## Prerequisites

- Docker installed on your machine
- Python 3.11 (for local development)

## Quick Start

### 1. Build the Docker Image

```bash
docker build -t flask-docker-app .
```

### 2. Run the Container

```bash
docker run -p 5000:5000 flask-docker-app
```

### 3. Access the Application

Open your browser or use curl to access: `http://127.0.0.1:5000`

## API Endpoints

### Home
```bash
curl http://127.0.0.1:5000/
```

### Get All Tasks
```bash
curl http://127.0.0.1:5000/tasks
```

### Get Task by ID
```bash
curl http://127.0.0.1:5000/tasks/101
```

### Create a New Task
```bash
curl -X POST http://127.0.0.1:5000/tasks \
  -H "Content-Type: application/json" \
  -d '{"id": 104, "name": "Deploy Application"}'
```

### More Task Creation Examples
```bash
# Create task: Backup Database
curl -X POST http://127.0.0.1:5000/tasks \
  -H "Content-Type: application/json" \
  -d '{"id": 105, "name": "Backup Database"}'

# Create task: Update Documentation
curl -X POST http://127.0.0.1:5000/tasks \
  -H "Content-Type: application/json" \
  -d '{"id": 106, "name": "Update Documentation"}'

# Create task: Run Tests
curl -X POST http://127.0.0.1:5000/tasks \
  -H "Content-Type: application/json" \
  -d '{"id": 107, "name": "Run Tests"}'
```

### Health Check
```bash
curl http://127.0.0.1:5000/health
```

## Docker Commands

### View Running Containers
```bash
docker ps
```

### View Container Logs
```bash
docker logs <container-id>
```

### Stop the Container
```bash
docker stop <container-id>
```

### Remove the Container
```bash
docker rm <container-id>
```

### Remove the Image
```bash
docker rmi flask-docker-app
```

## Project Structure

```
.
├── app.py              # Flask application
├── Dockerfile          # Docker configuration
├── requirements.txt    # Python dependencies
└── README.md          # This file
```

## Local Development (Without Docker)

```bash
# Install dependencies
pip install -r requirements.txt

# Run the application
python app.py
```

## Notes

- The application runs on port 5000
- Data is stored in memory and will be lost when the container stops
- Debug mode is enabled for development purposes

## Author

Shruti

## Repository

[docker-deploy](https://github.com/Shruti-lab/docker-deploy)
