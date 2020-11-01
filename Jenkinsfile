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
                    ls -al ${ALLURE_RESULT_PATH}
                    chmod -R o+xw ${ALLURE_RESULT_PATH}
                    ls -al ${ALLURE_RESULT_PATH}
                '''
            }
        }
        stage('Generate Allure Report') {
            steps{
                sh '''
                    export ALLURE_HOME=/allure-2.12.0
                    export PATH="${ALLURE_HOME}"/bin:$PATH
                    echo $PATH
                '''
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