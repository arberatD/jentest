pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/arberatD/jentest.git'
            }
        }

        stage('Setup Virtual Environment') {
            steps {
                sh '''
                python3 -m venv venv
                . venv/bin/activate
                '''
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '''
                . venv/bin/activate
                pip install -r requirements.txt
                '''
            }
        }

        stage('Run Tests') {
            steps {
                sh '''
                . venv/bin/activate
                pytest
                '''
            }
        }

        stage('Deploy') {
            when {
                // Nur ausführen, wenn alle vorherigen Stufen erfolgreich waren
                expression { currentBuild.result == 'SUCCESS' }
            }
            steps {
                sh '''
                . venv/bin/activate
                # Hier deinen Bereitstellungs-Script einfügen
                echo "Deploying application..."
                # Beispiel: python deploy.py
                '''
            }
        }
    }
}
