# Flask App Deployment to Azure App Service with GitHub Actions

This project demonstrates a simple CI/CD pipeline for deploying a Python Flask application to Azure App Service using GitHub Actions.

## What this project shows

- Basic Python Flask web application
- GitHub Actions workflow for build and deployment
- Azure App Service deployment using publish profile authentication
- CI/CD fundamentals for cloud-hosted applications

## Application routes

- `/` - main page
- `/health` - health check endpoint

## Technologies used

- Python
- Flask
- GitHub Actions
- Microsoft Azure App Service

## Pipeline flow

1. Code is pushed to the `main` branch
2. GitHub Actions installs dependencies
3. The workflow validates the Flask app
4. The application is packaged for deployment
5. The app is deployed automatically to Azure App Service

## Why I built this

I built this project to strengthen my hands-on DevOps skills in CI/CD, GitHub Actions, Azure App Service deployment, and Python-based application delivery.

## Skills demonstrated

- CI/CD pipeline creation
- GitHub Actions workflow configuration
- Azure App Service deployment
- Basic Python Flask application development
- Git-based automation workflow

## Notes

This project was built in a temporary sandbox Azure environment as part of my hands-on learning path toward Cloud Engineering and DevOps.