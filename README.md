# flask_redis_docker
This is a minimail containerized Flask app using Python 3.8 and Redis to as database.
#### Steps to get the app up and running:
```
$ docker-compose up --build
```
After build success, the web will be running on http://0.0.0.0:5000/ , if everything runs as expected you can see "Hello World! I have been seen {n} times."
(you will see the times you hit refresh, it expires after 60 sec.)

#### Activate python shell in a app container
```
$ docker exec -ti py_redis_app flask shell
```