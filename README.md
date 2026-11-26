# Movie Picture Pipeline

## 1. Project Overview

Movie Picture Pipeline is a containerized, cloud-deployed application that displays a list of movies through a React frontend and a backend REST API.

The project demonstrates automated CI/CD, Docker containerization, Amazon ECR image management, and Kubernetes deployment using Amazon EKS.

## 2. Project Architecture

```text
              Developer
                  |
                  v
              GitHub
                  |
                  v
          GitHub Actions
                  |
          +-------+-------+
          |               |
       Backend          Frontend
          CI/CD           CI/CD
          |               |
          v               v
       Docker           Docker
          |               |
          +-------+-------+
                  |
                  v
             Amazon ECR
                  |
                  v
              Amazon EKS
                  |
          +-------+-------+
          |               |
       Backend          Frontend
       Service          Service
          |               |
          +-------+-------+
                  |
             LoadBalancer
                  |
                  v
             Web Browser
```

## 3. Technologies Used

| Category | Technology |
|---|---|
| Frontend | React.js, JavaScript |
| Backend | Python |
| Containerization | Docker |
| Container Registry | Amazon ECR |
| Orchestration | Kubernetes |
| Cloud Platform | AWS |
| Kubernetes Service | Amazon EKS |
| CI/CD | GitHub Actions |
| Version Control | Git and GitHub |
| Authentication | GitHub OIDC with AWS IAM |

## 4. Project Features

- Display a list of movies.
- Fetch movie information from the backend REST API.
- Connect the React frontend with the backend.
- Build Docker images for frontend and backend.
- Push Docker images to Amazon ECR.
- Deploy containers on Amazon EKS.
- Expose applications through Kubernetes LoadBalancer services.
- Automate builds and deployments using GitHub Actions.

## 5. CI/CD Workflows

The project contains four GitHub Actions workflows:

| Workflow | Purpose |
|---|---|
| Backend CI | Backend build and validation |
| Backend CD | Build and deploy backend |
| Frontend CI | Frontend build and validation |
| Frontend CD | Build and deploy frontend |

The deployment workflows use AWS IAM OIDC authentication to obtain AWS credentials without storing long-lived AWS access keys in GitHub.

## 6. AWS Infrastructure

The project uses:

- Amazon ECR for storing Docker images.
- Amazon EKS for Kubernetes cluster management.
- AWS IAM for access management.
- AWS LoadBalancer services for application access.

**AWS Region:** us-east-1

**Kubernetes Cluster:** cluster

## 7. Application API

The backend provides a movies endpoint:

```text
GET /movies
```

Example response:

```json
{
  "movies": [
    {
      "id": "123",
      "title": "Top Gun: Maverick"
    },
    {
      "id": "456",
      "title": "Sonic the Hedgehog"
    },
    {
      "id": "789",
      "title": "A Quiet Place"
    }
  ]
}
```

## 8. Kubernetes Verification

The following commands were used to verify the deployment:

```bash
kubectl get nodes

kubectl get pods -A

kubectl get services -A

kubectl get deployments -A
```

The frontend and backend deployments were verified as ready, with their pods running successfully.

## 9. Deployment Results

The project achieved the following results:

- Frontend Docker image built successfully.
- Backend Docker image built successfully.
- Images pushed to Amazon ECR.
- Frontend deployed successfully on Amazon EKS.
- Backend deployed successfully on Amazon EKS.
- Frontend successfully connected to the backend API.
- Movie list displayed successfully in the browser.
- All four latest CI/CD workflow runs passed.

## 10. Live Application

**Frontend:**  
http://a2447188c077f4f8fb81950dda9225a9-148796412.us-east-1.elb.amazonaws.com

The deployed website successfully displays:

1. Top Gun: Maverick
2. Sonic the Hedgehog
3. A Quiet Place

## 11. Repository Structure

```text
cd12354-Movie-Picture-Pipeline/
│
├── .github/
│   └── workflows/
│       ├── backend-ci.yml
│       ├── backend-cd.yml
│       ├── frontend-ci.yml
│       └── frontend-cd.yml
│
├── starter/
│   ├── backend/
│   │   ├── k8s/
│   │   └── Dockerfile
│   │
│   └── frontend/
│       ├── k8s/
│       ├── src/
│       └── Dockerfile
│
└── README.md
```

*Note: This is the main project structure; additional application files and configuration files are present in the repository.*

## 12. Conclusion

The Movie Picture Pipeline project demonstrates an end-to-end DevOps workflow using AWS, Docker, Kubernetes, and GitHub Actions.

It successfully automates application builds and deployments, manages container images through Amazon ECR, and runs frontend and backend services on Amazon EKS.

The final application was tested through its public LoadBalancer endpoint, and the movie list was displayed successfully.
