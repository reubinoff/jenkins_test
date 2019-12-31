pipeline {
    agent { 
        docker {
            image "python:3.7"        
        } 
    }
    stages {
        stage('env') {
            steps {
                sh "mkdir /tmp/moshe"
                sh "HOME=/tmp/moshe pwd"
                sh """
                python -m pip install --user virtualenv
                python -m virtualenv venv --distribute
                . venv/bin/activate 
                pip install requirements.txt
                """
            }
        }
        stage('build') {
            steps {
                sh
                """
                . venv/bin/activate 
                python start_test.py
                """
            }
        }    
    }
    post { 
        always { 
            echo 'Stop everything!'
        }
    }
}