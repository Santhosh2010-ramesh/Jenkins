pipeline {
    agent any
    stages {
        stage('Clone Repository') {
            steps {
                git url:'https://github.com/Santhosh2010-ramesh/Jenkins.git',branch:'main'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'python3 -m venv venv'    // Create a virtual environment
                sh 'source venv/bin/activate && pip install -r requirements.txt'  // Activate the virtual environment and install dependencies
            }
        }

        stage('Run Tests') {
            steps {
                sh 'pytest tests/'
            }
        }

        stage('Build Artifact') {
            steps {
                sh 'python setup.py sdist'
            }
        }

        stage('Archive Artifact') {
            steps {
                archiveArtifacts artifacts: 'dist/*.tar.gz', fingerprint: true
            }
        }
    }
}

