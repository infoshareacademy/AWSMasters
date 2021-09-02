
```
apiVersion: apps/v1
kind: Deployment
metadata:
  creationTimestamp: null
  labels:
    run: www-app
  name: www-app
spec:
  replicas: 1
  selector:
    matchLabels:
      run: www-app
  template:
    metadata:
      creationTimestamp: null
      labels:
        run: www-app
    spec:
      containers:
      - image: REPLACE-ME
        name: www-app
        ports:
        - containerPort: 80

```