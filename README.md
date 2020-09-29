# Backend-app

## run locally

```bash
cd app

./start.sh
```

## run with docker

```bash
./start.sh
```

## Testing locally

<http://127.0.0.1:5002/health>

## Install on kubernetes

```bash
helm upgrade --install --namespace adsantos --create-namespace mydb helm
```

## Remote test

```bash
kubectl port-forward svc/front-app 5000:5000 -n adsantos

open http://127.0.0.1:5000/health
```
