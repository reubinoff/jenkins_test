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
                sh '''
                python -m pip install --user virtualenv
                python -m virtualenv venv --distribute
                . venv/bin/activate 
                pip install requirements.txt
                '''
            }
        }
        stage('build') {
            steps {
                sh 'python --version'
                sh
                '''
                . venv/bin/activate 
                python start_test.py
                '''
                timeout(time: 1, unit: 'MINUTES') {
                    retry(5) {
                        sh
                        '''
                        . venv/bin/activate 
                        python is_test_done.py
                        '''
                    }
                }
            }
        }    
    }
    post { 
        always { 
            echo 'Stop everything!'
        }
    }
}