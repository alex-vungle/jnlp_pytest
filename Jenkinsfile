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
    stages{
        stage('Foo') 
        {
            steps
            {
                sh '''
                    pytest --version
                    pip3 list
                    allure --version
                '''
            }
        }
    }
}