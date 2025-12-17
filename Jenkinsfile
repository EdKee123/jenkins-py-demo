pipeline{
    agent any

    enviroment{
        DOCkERHUB_CREDENTIALS = credentials('dockerhub-creds')
        DOCKER_REPO = "edkee123/my-flask-app"
    }

    stages{
        stage('Clone'){
            steps{
                git branch: 'main', url: 'https://github.com/EdKee123/jenkins-py-demo.git'
            }
        }

        stage('Build Docker Image'){
            steps{
                sh 'docker build -t $DOCKER_REPO:latest .'
            }
        }

        stage('Run Tests'){
            steps{
                sh 'docker run --rm $DOCKER_REPO:latest pytest || true'
            }
        }

        stage('Push to DockerHub'){
            steps{
                sh 'echo $DOCKERHUB_CREDENTIALS_PSW | docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin'
                sh 'docker push $DOCKER_REPO:latest'
            }
        }

        stage('Deploy with Helm'){
            steps{
                sh """
                helm upgrade --install my-flask-app ./charts/jenkins-py-demo \
                --set image.repository=$DOCKER_REPO
                --set image.tag=latest
                """
            }
        }
    }
}