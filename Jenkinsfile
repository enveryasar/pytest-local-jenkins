// pipeline{
//     agent any
//     // agent {
//     //     dockerfile true
//     // }
//     // agent any
//     // tools {dockerTool  "docker" } 
//     stages {
//         stage ('Test') {
//             agent {
//                  dockerfile true
//             }
//             steps {
//                 echo "HELLO WORLD"
//             }
//         }
//     }
// }


pipeline{
    agent {
        label 'docker'
    }
    stages {
        stage ('Test') {
            steps {
                echo "HELLO WORLD"
                sh 'docker build -t testImage .'
            }
        }
    }
}




// WORKED!
// pipeline{
//     agent none
//     stages {
//         stage ('Test') {
//             steps {
//                 echo "HELLO WORLD"
//             }
//         }
//     }
// }



// https://medium.com/swlh/build-your-first-automated-test-integration-with-pytest-jenkins-and-docker-ec738ec43955

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