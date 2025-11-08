pipeline {
    agent any
    triggers {
        pollSCM('H/2 * * * *')
    }
    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/HamedBouSaleh/video_store.git'
            }
        }
        stage('Build in Minikube Docker') {
            steps {
                sh '''
                #!/bin/bash
                eval $(/opt/homebrew/bin/minikube docker-env)
                /usr/local/bin/docker build -t videostoreapp:latest .
                '''
            }
        }
        stage('Deploy to Minikube') {
            steps {
                sh '''
                #!/bin/bash
                /opt/homebrew/bin/kubectl apply -f deployment.yaml
                /opt/homebrew/bin/kubectl apply -f service.yaml
                /opt/homebrew/bin/kubectl rollout status deployment/django-deployment
                '''
            }
        }
    }
}