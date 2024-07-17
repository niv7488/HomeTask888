#!groovy

pipeline {
    agent { 
        label 'Test_Agent'        
    }

    parameters {
        booleanParam(name: 'CLEAN_WS', defaultValue: true, description: 'Whether to cleanup the Jenkins workspace at the end of the execution.')
    }

    options {
        buildDiscarder(
            logRotator(numToKeepStr: '20')
        )
        ansiColor('xterm')
        timestamps()
        disableConcurrentBuilds()
        retry(3)
    }
    stages {
        stage('run task 1') {
            options {
                timeout(time: 15, unit: 'MINUTES')
            }            
            steps {
                    script {
                        env.RUN_TASK1 = "${sh(script: "bash Task1.sh", returnStdout: true).trim()}"
                        echo "${env.RUN_TASK1}"                                              
                        
                    }
                }
            }
        stage('run task 2') {
            options {
                timeout(time: 15, unit: 'MINUTES')
            }            
            steps {
                    script {
                        sh '''pip install fastapi kafka-python'''
                        env.RUN_TASK2 = "${sh(script: "python Task2.py", returnStdout: true).trim()}"
                        echo "${env.RUN_TASK2}"
                        env.RUN_TASK2_BASH = "${sh(script: "bash task2-bash.sh", returnStdout: true).trim()}"                                        
                        echo "${env.RUN_TASK2_BASH}" 
                    }
                }
            }            
        }
       
    post {     
        cleanup {
            script {
                if (params.CLEAN_WS.toBoolean()) {
                    cleanWs()
                }
            }
        }
    }
}

