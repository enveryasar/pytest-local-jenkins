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
    agent none
    stages {
        stage ('Test') {
            steps {
                echo "HELLO WORLD"
            }
        }
    }
}