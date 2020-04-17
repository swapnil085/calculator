pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                sh 'ls'
                sh 'curl -H "Content-Type: application/json" --data "{"build": true}" -X POST https://registry.hub.docker.com/u/swapnil085/calculator/trigger/a06de0ab-fb4a-43e1-bd3f-8b8aa7c65372/'
            }
        }
    }
}
