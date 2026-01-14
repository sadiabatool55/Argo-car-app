pipeline {
    agent {
        docker {
            image 'python:3.10-slim'
            args '-v /var/run/docker.sock:/var/run/docker.sock'
        }
    }

    environment {
        DOCKER_IMAGE = "sadia13/cars-app"
    }

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/sadiabatool55/Argo-car-app.git'
            }
        }

        stage('Build & Push Docker') {
            steps {
                script {
                    def appImage = docker.build("$DOCKER_IMAGE:latest", ".")
                    docker.withRegistry('', 'dockerhub-creds') {
                        appImage.push()
                    }
                }
            }
        }
    }
}
