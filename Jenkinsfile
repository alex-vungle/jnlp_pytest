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
                  name: test-runner
                spec:
                  containers:
                  - name: test_runner
                    image: sqli0189/jnlp-agent-pytest:latest
                    command:
                    - cat
                    tty: true
                  imagePullSecrets:
                    - name: vungleregistrykey
            '''
            defaultContainer 'test_runner'            
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