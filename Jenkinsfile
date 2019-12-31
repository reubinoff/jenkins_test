pipeline {
    agent { docker { image 'python:3.6' } }
    stages {
        stage('env') {
            steps {
                sh '''
                virtualenv venv --distribute
                . venv/bin/activate 
                pip install requirements.txt
                '''
            }
        }
        stage('build') {
            steps {
                sh 'python --version'
                sh 'python start_test.py'
                timeout(time: 1, unit: 'MINUTES') {
                    retry(5) {
                        sh 'python is_test_done.py'
                    }
                }
            }
        }
    }
}