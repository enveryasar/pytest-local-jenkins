pipeline{
    agent none
    // agent {
    //     dockerfile true
    // }
    // agent any
    // tools {dockerTool  "docker" } 
    stages {
        stage ('Test') {
            agent { docker 'openjdk:7'}
            steps {
                sh "java -version"
            }
        }
        stage ('Test1') {
            agent { docker 'openjdk:8'}
            steps {
                sh "java -version"
            }
        }
    }
}