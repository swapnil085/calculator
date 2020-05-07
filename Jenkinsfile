pipeline {
    environment {
        registry = "swapnil085/calculator"
        registryCredential = '4896be8b-c410-4e65-afee-fea935a8d05d'
        dockerImage = ''
    }
    agent any
    stages {
        stage('Build') {
            steps{
                script {
                    dockerImage = docker.build registry + ":$BUILD_NUMBER"
                }
            }
        }
        stage('test'){
            steps {
                sh 'pip3 install pytest'
                sh 'pytest'
            }
        }
        stage('Archive'){
            steps{
                script {
                    docker.withRegistry( '', registryCredential ) {
                    dockerImage.push()
                    }
                }
            }
        }
        stage('Deploy') {
            steps {
                build 'Rundeck_deploy'
            }
        }
    }
}
