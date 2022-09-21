pipeline{
    agent {
        dockerfile true
    }
    // agent any
    // tools {dockerTool  "docker" } 
    stages {
        stage ('Test') {
            steps {
                sh 'pytest -s --log-cli-level INFO'
                // sh '''
                // IMAGE_NAME="test-image"
                // CONTAINER_NAME="test-container"
                // echo "Check current working directory"
                // pwd
                // echo "Build docker image and run container"
                // docker build -t $IMAGE_NAME .
                // docker run -d --name $CONTAINER_NAME $IMAGE_NAME
                // echo "Copy result.xml into Jenkins container"
                // rm -rf reports; mkdir reports
                // docker cp $CONTAINER_NAME:/python-test/reports/result.xml reports/
                // echo "Cleanup"
                // docker stop $CONTAINER_NAME
                // docker rm $CONTAINER_NAME
                // docker rmi $IMAGE_NAME
                // '''
            }
        }
    }
}