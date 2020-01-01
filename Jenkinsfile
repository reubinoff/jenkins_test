pipeline {

    agent { 
        docker {
            image "python:3.7-alpine"        
        } 
    }


      environment {
        DISABLE_AUTH = 'true'
        DB_ENGINE    = 'sqlite'

    }

    
    stages {
        steps {
            withEnv(["HOME=${env.WORKSPACE}"]) {
                sh 'pip install --user virtualenv'
            }
        }
        stage('env') {
            steps {
                sh """
                python -m pip install --user virtualenv
                python -m virtualenv venv --distribute
                . venv/bin/activate 
                pip install requirements.txt
                """
            }
        }
        stage('run') {
            steps {
                echo "Start"
                sh """
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