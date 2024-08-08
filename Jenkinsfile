pipeline {
  agent any
  stages {
    stage('version') {
      steps {
        sh 'python3 --version'
      }
    }
    stage('Instalam pytest') {
      steps {
        sh 'pip install pytest pytest-cov'
        sh 'pytest test.py --doctest-modules --junitxml=junit/test-results.xml --cov=com --cov-report=xml --cov-report=html'
      }
    }
  }
}