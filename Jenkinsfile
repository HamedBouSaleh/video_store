pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/HamedBouSaleh/video_store.git'
            }
        }

        stage('Build in Minikube Docker') {
            steps {
                script {
                    // Make sure we're using Minikube's Docker environment
                    sh 'eval $(minikube docker-env)'
                    sh 'docker build -t video-store:latest .'
                }
            }
        }

        stage('Run Container in Minikube') {
            steps {
                script {
                    sh 'kubectl delete pod video-store-pod --ignore-not-found=true'
                    sh 'kubectl run video-store-pod --image=video-store:latest --restart=Never'
                }
            }
        }
    }
}
