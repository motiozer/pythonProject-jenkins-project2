pipeline {
    agent any
    stages {
        stage('checkout') {
            steps {
                script {
                    properties([pipelineTriggers([pollSCM('* * * * *')])])
                }
                git 'https://github.com/motiozer/pythonProject-jenkins-project2.git'
            }
        }
        stage('run rest server') {
            steps {
                bat 'start /min python rest_app.py'
				
                }
        }
		stage('run web server') {
            steps {
				bat 'start /min python web_app.py'
				
                }
        }
				stage('run backend_testing') {
            steps {
					bat 'python backend_testing.py'
				
                }
        }
				stage('run Frontend_testing') {
            steps {
					bat 'python frontend_testing.py'
				
                }
        }
				stage('run combined_testing') {
            steps {
					bat 'python combined_test.py'
				
                }
        }
				stage('clean_environemnt') {
            steps {
					bat 'python clean_environment.py'
				
                }
        }
		
    }
}
