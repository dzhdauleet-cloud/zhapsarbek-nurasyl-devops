pipeline {
    agent any

    environment {
        STUDENT_NAME = 'Nurasyl'
        STUDENT_SURNAME = 'Zhapsarbek'
        STUDENT_GROUP = 'IT2-2308'
        STUDENT_ID = '37841'
        PATH+DOCKER = '/Users/nurasylzapsarbek/.docker/bin'
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
                sh 'git log -1 --oneline'
            }
        }

        stage('Build') {
            steps {
                sh 'python3 -m py_compile app/app.py'
            }
        }

        stage('Test') {
            steps {
                sh 'python3 -m unittest discover -s tests -v'
            }
        }

        stage('Docker Build') {
            steps {
                sh 'docker build -t zhapsarbek-nurasyl-devops .'
            }
        }

        stage('Docker Run') {
            steps {
                sh '''
                    echo "Student: $STUDENT_NAME $STUDENT_SURNAME"
                    echo "Group: $STUDENT_GROUP"
                    echo "Student ID: $STUDENT_ID"

                    docker rm -f zhapsarbek-nurasyl-jenkins >/dev/null 2>&1 || true

                    docker run -d \
                      --name zhapsarbek-nurasyl-jenkins \
                      -p 8082:8080 \
                      -e STUDENT_NAME \
                      -e STUDENT_SURNAME \
                      -e STUDENT_GROUP \
                      -e STUDENT_ID \
                      zhapsarbek-nurasyl-devops

                    curl --retry 10 --retry-connrefused \
                      --retry-delay 1 -fsS \
                      http://localhost:8082/ > response.txt

                    cat response.txt
                    grep -q "Application is running successfully!" response.txt
                '''
            }
        }
    }
}
