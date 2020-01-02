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
        stage('Create List') {
            steps {
                script {
                    // you may create your list here, lets say reading from a file after checkout
                    list = ["Test-1", "Test-2", "Test-3", "Test-4", "Test-5"]
                }
            }
        }
        stage('run') {
             steps {
                script {
                     parallel {
                    for(int i=0; i < 1000; i++) {
                        def t = "test " + Integer.toString(i)
                        stage(t){
                            steps {
                                sh """
                                    . venv/bin/activate 
                                    python start_test.py
                                """
                            }
                        }
                    }
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