pipeline {
  agent any
  stages {
    stage('build') {
      steps {
        sh 'echo "TEST"'
        echo 'TEST'
      }
    }

    stage('test') {
      steps {
        echo 'TESTING THE PROGRAM'
      }
    }

    stage('deploy') {
      steps {
        sh '''max=1000
for i in `seq 2 $max`
do
    echo "$i"
done'''
      }
    }

  }
}