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
        stage('test'){
            steps {
                withEnv(["HOME=${env.WORKSPACE}"]) {
                    sh 'pip install --user virtualenv'
                      sh """
                            python -m pip install --user virtualenv
                            python -m virtualenv venv --distribute
                            . venv/bin/activate 
                            pip install -r requirements.txt
                        """
                }
            }
        }
        
        stage('run') {
             parallel {
                 stage('suite a') {
                    steps {
                        echo "Start"
                        sh """
                        . venv/bin/activate 
                        python start_test.py
                        """
                    }
                }
                stage('suite b') {
                    steps {
                        echo "Start"
                        sh """
                        . venv/bin/activate 
                        python start_test.py
                        """
                    }
                }
                stage('suite c') {
                    steps {
                        echo "Start"
                        sh """
                        . venv/bin/activate 
                        python start_test.py
                        """
                    }
                }
                stage('suite d') {
                    steps {
                        echo "Start"
                        sh """
                        . venv/bin/activate 
                        python start_test.py
                        """
                    }
                }
                stage('suite e') {
                    steps {
                        echo "Start"
                        sh """
                        . venv/bin/activate 
                        python start_test.py
                        """
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