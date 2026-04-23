pipeline {
    agent any

    stages {
        stage('Setup Python') {
            agent {
                docker {
                    image 'python3-alpine'
                }
            }
            steps {
                
                sh '''
                ls -la
                python --version

                '''
            }
        }

        stage('Run Tests') {
            steps {
                sh 'test -f app.py'
            }
        }
    }
}