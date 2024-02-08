pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/arberatD/jentest.git'
            }
        }

        stage('Run Script') {
            steps {
                sh 'python3 hi.py'
            }
        }
    }
}
