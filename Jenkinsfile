pipeline
{
    agent 
    {
        kubernetes
        {
            yaml '''
                apiVersion: v1
                kind: Pod
                metadata:
                  name: testrunner
                spec:
                  containers:
                  - name: testrunner
                    image: sqli0189/jnlp-agent-pytest:latest
                    command:
                    - cat
                    tty: true
            '''
            defaultContainer 'testrunner'            
        }
    }
    environment {
        ALLURE_RESULT_PATH = './target/allure-result'
    }
    stages{
        stage('Execute Automation Test') 
        {
            steps
            {
                sh '''
                    pytest test_foo.py --alluredir=${ALLURE_RESULT_PATH} || true
                    chmod -R o+xw ${ALLURE_RESULT_PATH}
                '''
            }
        }
        stage('Generate Allure Report') {
            steps{
                script {
                    allure([
                        includeProperties: false,
                        jdk: '',
                        properties: [],
                        reportBuildPolicy: 'ALWAYS',
                        results: [[path: 'target/allure-result']]])
                }
            }
        }
    }
}