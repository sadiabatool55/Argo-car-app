pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "sadia13/cars-app"
    }

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/sadiabatool55/Argo-car-app.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    docker.build("${DOCKER_IMAGE}:latest")
                }
            }
        }

        stage('Push Docker Image') {
            steps {
                script {
                    docker.withRegistry('', 'dockerhub-creds') {
                        docker.image("${DOCKER_IMAGE}:latest").push()
                    }
                }
            }
        }
    }
}
