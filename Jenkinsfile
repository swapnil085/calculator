pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                sh 'ls'
                sh 'curl -H "Content-Type: application/json" --data "{"build": true}" -X POST https://registry.hub.docker.com/u/swapnil085/calculator/trigger/d4bdafcd-8b0c-42db-8b50-adbf006a888d/'
            }
        }
        stage('test'){
            steps {
                sh 'pip3 install pytest'
                sh 'pytest'
            }
        }
        stage('Deploy') {
            steps {
                build 'Rundeck_deploy'
            }
        }
    }
}
