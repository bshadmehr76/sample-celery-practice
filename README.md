# README #

This documentation explains about celery
I have implemented two simple use case

### use case 1: ###

* user calls an api
* api calls a task that generates a pdf
* we store the task id
* user can check pdf generation status using another route

### use case 2: ###

* we use celery beat to check our ping
* we store the ping and it's status in db
* user can check the ping hostory using an api

### requirements ###

* install requirements modules
* install and run redis, you can achieve this by docker: docker run -d -p 6379:6379 redis
* run celery and celery beat via celery -A tasks worker -l INFO, celery -A tasks beat -l INFO