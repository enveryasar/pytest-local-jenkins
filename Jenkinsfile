pipeline {
    agent any
    tools {nodejs "node"} // update with pytest
    stages {
        stage('Build & Run tests') {
            parallel {
                stage('Run API tests') {
                    steps {
                        script {
                            try {
                                sh 'pip install -r requirements.txt'
                                    sh("TEST_CONFIG=${params.ENVIRONMENT} CLIENT_SECRET=$STAGE_CLIENT_SECRET python3 -m pytest -v tests/* --reruns 2 --reruns-delay 5 -s --junitxml=results.xml")
                                } 
                            catch (Exception e) {
                                }
                        }
                    }
                    post {
                        always {
                            stash includes: 'results.xml', name: 'api-results'
                            archiveArtifacts artifacts: 'results.xml'
                        }
                    }
                }
            }
        }
    }
}