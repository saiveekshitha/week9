pipeline {
    agent any
    stages {
        stage('Build Docker Image') {
            steps {
                bat 'docker build -t registration:v1 .'
            }
        }
        stage('Push to Docker Hub') {
            steps {
                bat 'docker tag registration:v1 saiveekshithakande/registration:v1'
                bat 'docker push saiveekshithakande/registration:v1'
            }
        }
        stage('Deploy to Kubernetes') {
            steps {
                bat 'kubectl apply -f C:/DevOps/week2/deployment.yaml'
                bat 'kubectl apply -f C:/DevOps/week2/service.yaml'
            }
        }
        stage('Automated UI Test') {
        steps {
            bat 'python C:/DevOps/week2/test_registration.py';
        }
        }
    }
}
