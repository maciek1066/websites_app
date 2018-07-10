from celery import Celery

app = Celery('tasks', broker='amqp://localhost/')

@app.task
def reverse(string):
    return string[::-1]
