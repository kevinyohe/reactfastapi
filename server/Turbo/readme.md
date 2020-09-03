# Turbo
Data for testing react frontend

#### Running - python main.py (uvicorn)
```
(venv) kevin@Kevins-MBP Turbo % python main.py 
INFO:     Started server process [12534]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)
INFO:     127.0.0.1:63233 - "GET / HTTP/1.1" 200 OK
```

## Docker
### Setup
```
Initial:
  docker build -t myimage .
running: 
  docker run -d --name mycontainer -p 80:80 myimage
rebuild or setup the volume option and restart automatically
restart:
  docker start mycontainer
```