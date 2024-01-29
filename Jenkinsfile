pipeline {
    agent {
        docker {
            image 'python:3.11.3'
        }
    }

    stages {
        stage('Build') {
            steps {
                script {
                    // Do any build steps here, if needed
                }
            }
        }

        stage('Test') {
            steps {
                script {
                    // Install dependencies if needed
                    sh 'pip install pytest'

                    // Run tests and generate HTML report
                    sh 'pytest --html=report.html test_my_functions_MySQL.py'
                }
            }

            post {
                always {
                    // Archive the HTML report as an artifact
                    archiveArtifacts 'report.html'
                }
            }
        }
    }
}
