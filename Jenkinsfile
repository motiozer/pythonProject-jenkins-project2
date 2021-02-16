pipeline {
  agent any
  stages {
    stage('rest_app.py') {
      steps {
        bat(script: 'python C:\\Users\\motioz\\pythonProject-jenkins-project2\\rest_app.py', label: 'enable_rest_app')
      }
    }

    stage('web_app.py') {
      steps {
        bat(script: 'python C:\\Users\\motioz\\pythonProject-jenkins-project2\\web_app.py', label: 'enable_web')
      }
    }

  }
}