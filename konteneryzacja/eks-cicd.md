```
version: 0.2

phases:
  pre_build:
    commands:
      - echo Logging in to Amazon ECR...
      - aws --version
      - aws ecr get-login-password --region eu-west-1 | docker login --username AWS --password-stdin 213141549337.dkr.ecr.eu-west-1.amazonaws.com
      - REPOSITORY_URI=213141549337.dkr.ecr.eu-west-1.amazonaws.com/k8s-php-app-repo
      - COMMIT_HASH=$(echo $CODEBUILD_RESOLVED_SOURCE_VERSION | cut -c 1-7)
      - IMAGE_TAG=${COMMIT_HASH:=latest}
  build:
    commands:
      - echo Build started on `date`
      - echo Building the Docker image...
      - docker build -t $REPOSITORY_URI:latest .
      - docker tag $REPOSITORY_URI:latest $REPOSITORY_URI:$IMAGE_TAG
  post_build:
    commands:
      - echo Build completed on `date`
      - echo Pushing the Docker images...
      - docker push $REPOSITORY_URI:latest
      - docker push $REPOSITORY_URI:$IMAGE_TAG
      - echo Writing image definitions file...
      - aws ssm put-parameter --name image --value $REPOSITORY_URI:$IMAGE_TAG --overwrite

```


```
version: 0.2

phases:
  build:
    commands:
      - IMAGE=$(aws ssm get-parameters --names "image" --query 'Parameters[0].Value' --output text)
      - START="www-app="
      - UPDATECOMMAND=$START$IMAGE
      - aws eks --region eu-west-1 update-kubeconfig --name awsmasters-k8s
      - kubectl set image deployment/www-app $UPDATECOMMAND
```