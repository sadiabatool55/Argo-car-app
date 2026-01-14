pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "dockerhub-username/cars-app"
    }

    stages {
        stage('Checkout') {
            steps {
                git(
                    url: 'https://github.com/sadiabatool55/Argo-car-app.git',
                    branch: 'main',
                    credentialsId: 'github-connect'
                )
            }
        }

        stage('Build Image') {
            steps {
                bat 'docker build -t $DOCKER_IMAGE:latest app/'
            }
        }

        stage('Push Image') {
            steps {
                withDockerRegistry([credentialsId: 'dockerhub-creds']) {
                    bat 'docker push $DOCKER_IMAGE:latest'
                }
            }
        }
    }
}
