ppipeline {
    agent any
    environment {
        PATH = "/usr/local/bin:/opt/homebrew/bin:${env.PATH}"
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
                    echo "PATH is: $PATH"
                    eval $(minikube docker-env)
                    docker build -t videostoreapp:latest .
                '''
            }
        }
        stage('Deploy to Minikube') {
            steps {
                sh '''
                    kubectl apply -f deployment.yaml
                    kubectl apply -f service.yaml
                    kubectl rollout status deployment/django-deployment
                '''
            }
        }
    }
}
