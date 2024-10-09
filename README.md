# Rick and Morty Character API

This project queries the Rick and Morty API to find characters that meet specific criteria and provides a REST API to access the data.

## Features

- Queries the Rick and Morty API for characters that are:
  - Human
  - Alive
  - From Earth (C-137)
- Creates a CSV file with the results
- Provides a REST API to access the data
- Includes a health check endpoint
- Containerized with Docker
- Kubernetes deployment ready
- Helm chart for easy deployment

## Prerequisites

- Python 3.9+
- Docker
- Kubernetes cluster (can be local with minikube/microk8s)
- Helm

## Running Locally

1. Install dependencies:
```
pip install -r requirements.txt
```

2. Run the application:
```
python app.py
```

## Docker

Build the Docker image:
```
docker build -t rickmorty-app .
```

Run the container:
```
docker run -p 5000:5000 rickmorty-app
```

## Kubernetes Deployment

Apply the Kubernetes manifests:
```
kubectl apply -f yamls/
```

## Helm Deployment

Install the Helm chart:
```
helm install rickmorty helm/rickmorty
```

## API Endpoints

- GET `/characters` - Returns the list of characters
- GET `/healthcheck` - Returns the health status of the application

## CSV Output

The application generates a CSV file named `characters.csv` with the following columns:
- Name
- Location
- Image