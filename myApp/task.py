import time
from celery import task

def sun():
    print("sun is the entry!")
    time.sleep(5)
    print("sun is the entry!")