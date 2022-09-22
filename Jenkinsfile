pipeline{
    agent {
        label 'docker'
    }
    stages {
        stage ('BUILD IMAGE') {
            steps {
                sh 'docker build -t test-image .'
            }
        }
        stage ('RUN TEST IN A CONTAINER - ARTIFACT') {
            steps {
                sh 'docker run --name test-container -v $(pwd):/python-test test-image pytest --junitxml=reports/result.xml -s --log-cli-level INFO'
                sh "docker cp test-container:/python-test/reports/ ${WORKSPACE}/test-results"
            }
            post {
                always {
                    dir("${WORKSPACE}"){
                        stash includes: "test-results/result.xml", name: 'results-stashed'
                        archiveArtifacts artifacts: 'test-results/result.xml'
                    }
                }
            }
        }
        stage ('DELETE IMAGE-CONTAINER-TESTRESULTS') {
            steps {
                sh 'docker rm test-container'
                sh 'docker rmi test-image'
                sh "rm -r ${WORKSPACE}/reports/"
                sh "rm -r ${WORKSPACE}/test-results/"
            }
        }
    }
}