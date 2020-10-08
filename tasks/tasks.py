from .celery import app
import time
import random


@app.task
def create_pdf():
    time.sleep(15)
    return True

@app.task
def email_users():
    time.sleep(60)
    return True

@app.task
def system_ping_check():
    with open('ping_status.csv.db', 'a+') as db:
        if random.randint(0,100) > 50:
            db.write(str(int(time.time())) + ",success\n")
        else:
            db.write(str(int(time.time())) + ",faliure\n")
    return True
