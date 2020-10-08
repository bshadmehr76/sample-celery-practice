from celery import Celery
from celery.schedules import crontab


app = Celery('tasks',
             broker='redis://localhost',
             backend='redis://localhost',
             include=['tasks.tasks'])

app.conf.update(
    result_expires=3600,
)

app.conf.beat_schedule = {
    "system-health-check": {
        "task": "tasks.tasks.system_ping_check",
        "schedule": 10.0
    }
}

if __name__ == '__main__':
    app.start()