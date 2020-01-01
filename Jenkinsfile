pipeline {

    agent { 
        docker {
            image "python:3.7"        
        } 
    }


      environment {
        DISABLE_AUTH = 'true'
        DB_ENGINE    = 'sqlite'
        PYENV_HOME=$WORKSPACE'/.pyenv/'

    }

    
    stages {
        stage('env') {
            steps {
                sh """
                virtualenv --no-site-packages venv
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