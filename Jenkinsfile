pipeline {
    agent any


    stages {
        
        stage('Docker Compose') {
            when {
                branch 'feature-*'
            }
            steps {
                sh '''
                export PATH=/sbin:/usr/sbin:/bin:/usr/bin:/usr/local/bin/
                /usr/local/bin/docker-compose up -d --build
                '''
            }
        }

        stage('Test') {
            when {
                branch 'feature-*'
            }
            steps {
                sh '''
                /Users/clementboulanger/opt/anaconda3/bin/python -m pip install --upgrade pip
                /Users/clementboulanger/opt/anaconda3/bin/pip install -r ./web/requirements.txt
                /Users/clementboulanger/opt/anaconda3/bin/python -m pytest ./tests
                '''
            }
        }

        stage('Deploy to develop') {
            when{
                branch 'feature-*'
            }
            steps{
                sh '''
                git config --global user.email "clement.boulanger@efrei.net"
                git config --global user.name "ClementBou"
                git config pull.rebase true
                git fetch --all
                git config remote.origin.fetch '+refs/heads/*:refs/remotes/origin/*'
                git checkout ${GIT_BRANCH}
                git pull
                git checkout develop
                git pull
                git merge ${GIT_BRANCH}
                git push
                '''
            }
        }

        stage('Release') {
            when {
                branch 'develop'
            }
            steps {
                sh '''
                /usr/local/bin/brew install hub
                git config --global user.email "clement.boulanger@efrei.net"
                git config --global user.name "ClementBou"
                git config pull.rebase true
                git fetch --all
                git config remote.origin.fetch '+refs/heads/*:refs/remotes/origin/*'
                git checkout main
                git pull
                git checkout develop
                git pull
                /usr/local/bin/hub pull-request --message 'Release' --base main --head develop
                '''
            }
        }

    }
}


