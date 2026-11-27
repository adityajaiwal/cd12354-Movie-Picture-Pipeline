# Movie Picture Pipeline

## 1. Project Overview

Movie Picture Pipeline is a containerized, cloud-deployed application that displays a list of movies through a React frontend and a Python Flask backend REST API.

The project demonstrates an end-to-end DevOps workflow using Docker, Kubernetes, Amazon Web Services (AWS), Amazon Elastic Kubernetes Service (EKS), Amazon Elastic Container Registry (ECR), and GitHub Actions.

The application is deployed on AWS EKS, with separate frontend and backend services exposed through AWS LoadBalancers.

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
             +---------+---------+
             |                   |
         Backend               Frontend
           CI/CD                 CI/CD
             |                   |
             v                   v
        Docker Build        Docker Build
             |                   |
             v                   v
        Amazon ECR           Amazon ECR
             |                   |
             +---------+---------+
                       |
                       v
                  Amazon EKS
                       |
              +--------+--------+
              |                 |
          Backend             Frontend
         Deployment          Deployment
              |                 |
          Backend             Frontend
           Service             Service
              |                 |
          LoadBalancer       LoadBalancer
              |                 |
              v                 v
         Backend API        Web Browser
              ^
              |
         React Frontend
```

## 3. Technologies Used

| Category | Technology |
|---|---|
| Frontend | React.js, JavaScript |
| Backend | Python, Flask |
| Containerization | Docker |
| Container Registry | Amazon ECR |
| Orchestration | Kubernetes |
| Cloud Platform | AWS |
| Kubernetes Service | Amazon EKS |
| CI/CD | GitHub Actions |
| Version Control | Git and GitHub |
| Authentication | GitHub OIDC with AWS IAM |

## 4. Project Features

- Display a list of movies through a React frontend.
- Fetch movie information from the backend REST API.
- Connect the frontend with the backend.
- Build Docker images for frontend and backend.
- Push Docker images to Amazon ECR.
- Deploy containers on Amazon EKS.
- Expose frontend and backend through Kubernetes LoadBalancer services.
- Automate frontend and backend builds using GitHub Actions.
- Automate deployments using GitHub Actions.
- Authenticate GitHub Actions with AWS using OpenID Connect (OIDC).

## 5. CI/CD Workflows

The repository contains four GitHub Actions workflows.

| Workflow | Purpose |
|---|---|
| Backend CI | Backend linting, testing and Docker image build |
| Backend CD | Backend Docker image build and deployment |
| Frontend CI | Frontend linting and testing |
| Frontend CD | Frontend validation, Docker image build and deployment |

### Backend Continuous Integration

The backend CI workflow performs:

1. Checkout repository.
2. Set up Python 3.10.
3. Install backend dependencies using Pipenv.
4. Run Flake8 for code quality.
5. Execute backend tests using Pytest.
6. Build the backend Docker image.

### Frontend Continuous Integration

The frontend CI workflow performs:

1. Checkout repository.
2. Set up Node.js 18.
3. Install dependencies using npm.
4. Run ESLint.
5. Execute frontend tests.

### Backend Continuous Deployment

The backend CD workflow performs:

1. Checkout repository.
2. Configure AWS credentials using GitHub OIDC.
3. Authenticate with Amazon ECR.
4. Build the backend Docker image.
5. Push the image to Amazon ECR.
6. Update Kubernetes configuration.
7. Deploy the backend image to Amazon EKS.
8. Verify deployment rollout status.

### Frontend Continuous Deployment

The frontend CD workflow performs:

1. Checkout repository.
2. Run frontend linting and testing.
3. Configure AWS credentials using GitHub OIDC.
4. Authenticate with Amazon ECR.
5. Build the frontend Docker image.
6. Push the frontend image to Amazon ECR.
7. Update Kubernetes configuration.
8. Deploy the frontend image to Amazon EKS.
9. Verify deployment rollout status.

## 6. AWS Infrastructure

The project uses the following AWS services:

- **Amazon ECR:** Stores frontend and backend Docker images.
- **Amazon EKS:** Manages the Kubernetes cluster.
- **AWS IAM:** Provides access management and permissions.
- **AWS Elastic Load Balancing:** Exposes frontend and backend services publicly.

**AWS Region:** `us-east-1`

**Kubernetes Cluster:** `cluster`

**Kubernetes Namespace:** `default`

**Authentication:** GitHub Actions OIDC with AWS IAM Role.

## 7. Application API

The backend provides a REST API endpoint to retrieve movie information.

**HTTP Method:** GET

**API Endpoint:**

```text
/movies
```

**Backend API URL:**

http://a13570bdc57024ba5b27d75ab910533a-111264564.us-east-1.elb.amazonaws.com/movies

### Example API Response

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

### API Testing Results

The backend API was successfully tested using AWS CloudShell and Windows Command Prompt.

**Verified HTTP Response:**

```text
HTTP/1.1 200 OK
Content-Type: application/json
```

The API returned the expected JSON response containing all three movies.

**Important:** The backend application exposes the `/movies` endpoint. Opening the backend LoadBalancer root URL without `/movies` returns `404 Not Found` because a root route is not configured. This does not indicate that the API is down.

## 8. Live Application

The application was deployed through separate AWS LoadBalancer endpoints.

### Frontend Application

**URL:**

http://a2447188c077f4f8fb81950dda9225a9-148796412.us-east-1.elb.amazonaws.com

The React frontend successfully displays the following movies:

1. Top Gun: Maverick
2. Sonic the Hedgehog
3. A Quiet Place

### Backend REST API

**URL:**

http://a13570bdc57024ba5b27d75ab910533a-111264564.us-east-1.elb.amazonaws.com/movies

The backend API returns movie information in JSON format.

## 9. Kubernetes Verification

The following commands were used to verify the Kubernetes deployment.

### Check Kubernetes Nodes

```bash
kubectl get nodes
```

### Check Running Pods

```bash
kubectl get pods -A
```

### Check Kubernetes Services

```bash
kubectl get services -A
```

### Check Deployments

```bash
kubectl get deployments -A
```

### Check Backend Service

```bash
kubectl get svc movie-backend -n default
```

### Check Frontend Service

```bash
kubectl get svc frontend -n default
```

### Test Backend API

```bash
curl -i http://a13570bdc57024ba5b27d75ab910533a-111264564.us-east-1.elb.amazonaws.com/movies
```

### Verify Backend LoadBalancer DNS

```bash
kubectl get svc movie-backend -n default -o wide
```

The backend API returned an HTTP 200 OK response with the expected movie information.

## 10. Deployment Results

The following project milestones were successfully completed:

- Frontend Docker image built successfully.
- Backend Docker image built successfully.
- Docker images pushed to Amazon ECR.
- Frontend deployed on Amazon EKS.
- Backend deployed on Amazon EKS.
- Frontend and backend LoadBalancer services created.
- Backend API successfully tested using AWS CloudShell.
- Backend API successfully accessed from Windows Command Prompt.
- DNS resolution verified using Google DNS.
- Frontend successfully connected to the backend API.
- Movie list displayed successfully in the browser.
- Backend CI workflow executed successfully.
- Frontend CI workflow executed successfully.
- Backend CD workflow executed successfully.
- Frontend CD workflow executed successfully.

## 11. Repository Structure

```text
cd12354-Movie-Picture-Pipeline/
│
├── .github/
│   └── workflows/
│       ├── backend-cd.yml
│       ├── backend-ci.yaml
│       ├── frontend-cd.yaml
│       └── frontend-ci.yaml
│
├── starter/
│   ├── backend/
│   │   ├── k8s/
│   │   ├── Dockerfile
│   │   └── application files
│   │
│   └── frontend/
│       ├── k8s/
│       ├── src/
│       ├── Dockerfile
│       └── application files
│
├── .gitignore
├── CODEOWNERS
├── LICENSE.md
└── README.md
```

*Note: This represents the main project structure. Additional application files and configuration files are present in the repository.*

## 12. Conclusion

The Movie Picture Pipeline project demonstrates a complete DevOps deployment workflow using AWS, Docker, Kubernetes, Amazon ECR, Amazon EKS, and GitHub Actions.

The project successfully automates application validation, Docker image creation, image management, and Kubernetes deployments.

Both frontend and backend services were deployed on Amazon EKS and exposed through AWS LoadBalancers.

The backend REST API successfully returned the expected movie information, and the React frontend displayed the movie list in the browser.

This project demonstrates practical experience with:

- Cloud infrastructure using AWS.
- Containerization using Docker.
- Container orchestration using Kubernetes.
- CI/CD automation using GitHub Actions.
- Container image management using Amazon ECR.
- Application deployment using Amazon EKS.
- Secure AWS authentication using GitHub OIDC.

---

## Project Information

**Project Name:** Movie Picture Pipeline

**Project Status:** Successfully Completed

**Cloud Platform:** Amazon Web Services (AWS)

**AWS Region:** us-east-1

**Kubernetes Cluster:** cluster

**Deployment Platform:** Amazon EKS

**Container Registry:** Amazon ECR

**CI/CD:** GitHub Actions

**Version Control:** Git and GitHub
