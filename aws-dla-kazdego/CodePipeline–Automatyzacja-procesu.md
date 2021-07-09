Skrypt buildspec dla CodeBuild

```
version: 0.2
phases:
  build:
    commands:
    - touch test.txt
    - echo "To jest jakis tekst" > test.txt
artifacts:
  files:
    - '**/*'
```
