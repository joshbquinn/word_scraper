node {

    notify('CI')
    try {

        stage('Checkout') {
            checkout scm
        }

        stage('Run'){

            bat 'py create_word_check_lists.py'
            bat 'py main.py'
        }

    } catch (err) {
        notify("Error ${err}")
        currentBuild.result = 'FAILURE'
    }
}

def notify(status){
    emailext (
            to: "jbqjenkins@gmail.com",
            subject: "${status}: Job '${env.JOB_NAME} [${env.BUILD_NUMBER}]'",
            body: """<p>${status}: Job '${env.JOB_NAME} [${env.BUILD_NUMBER}]':</p>
        <p>Check console output at <a href='${env.BUILD_URL}'>${env.JOB_NAME} [${env.BUILD_NUMBER}]</a></p>""",
    )
}