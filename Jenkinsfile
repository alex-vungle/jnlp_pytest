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
                  imagePullSecrets:
                    - name: vungleregistrykey
            '''
            defaultContainer 'testrunner'            
        }
    }
    environment {
        ALLURE_RESULT_PATH = './target/allure-result'
    }
    stages{
        stage('Foo') 
        {
            steps
            {
                sh '''
                    pytest test_foo.py --alluredir=${ALLURE_RESULT_PATH} || true
                '''
            }
        }
    }
}