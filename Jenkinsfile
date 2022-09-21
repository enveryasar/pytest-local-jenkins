pipeline{
    // agent {
    //     dockerfile true
    // }
    // agent any
    // tools {dockerTool  "docker" } 
    stages {
        stage ('Test') {
            agent {
                 dockerfile true
            }
            steps {
                echo "HELLO WORLD"
            }
        }
    }
}