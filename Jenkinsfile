pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "dockerhub-username/cars-app"
    }

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/sadiabatool55/Argo-car-app.git'
            }
        }

        stage('Build Image') {
            steps {
                sh 'docker build -t $DOCKER_IMAGE:latest app/'
            }
        }

        stage('Push Image') {
            steps {
                withDockerRegistry([credentialsId: 'dockerhub-creds']) {
                    sh 'docker push $DOCKER_IMAGE:latest'
                }
            }
        }
    }
}
