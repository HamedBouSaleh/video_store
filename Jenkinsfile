pipeline {
    agent any

    environment {
        // Append to PATH correctly
        PATH = "$PATH:/usr/local/bin:/opt/homebrew/bin"
    }

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
                    echo ">>> Setting up Minikube Docker environment"
                    eval $(minikube docker-env)
                    echo ">>> Building Docker image inside Minikube"
                    docker build -t videostoreapp:latest .
                '''
            }
        }

        stage('Deploy to Minikube') {
            steps {
                sh '''
                    echo ">>> Deploying to Minikube"
                    kubectl apply -f deployment.yaml
                    kubectl apply -f service.yaml
                    kubectl rollout status deployment/django-deployment
                '''
            }
        }
    }
}
