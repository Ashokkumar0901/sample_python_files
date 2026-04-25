pipeline {
    agent any

    stages {
        stage('Setup Python') {
            steps {
                sh '''
                ls -la
                python3 --version
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