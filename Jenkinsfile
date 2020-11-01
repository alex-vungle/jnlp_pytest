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
                  name: testRunner
                spec:
                  containers:
                  - name: testRunner
                    image: sqli0189/jnlp-agent-pytest:latest
                    command:
                    - cat
                    tty: true
                  imagePullSecrets:
                    - name: vungleregistrykey
            '''
            defaultContainer 'testRunner'            
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