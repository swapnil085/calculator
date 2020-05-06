pipeline {
    environment {
    registry = "swapnil085/calculator"
    registryCredential = 'Swapnil@123'
    dockerImage = ''
    dockerImageLatest = ''
  }
    agent any
    stages {
        stage('Build') {
            steps{
                script {
                    dockerImage = docker.build registry + ":$BUILD_NUMBER"
                    dockerImageLatest = docker.build registry + ":latest"
                }
            }
        }
        stage('test'){
            steps {
                sh 'pip3 install pytest'
                sh 'pytest'
            }
        }
        stage('Archive Image'){
            steps{
                script {
                        docker.withRegistry( '', registryCredential ) {
                        dockerImage.push()
                        dockerImageLatest.push()
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
