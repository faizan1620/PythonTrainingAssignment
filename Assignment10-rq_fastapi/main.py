from module.process_messages import process_message, report_failure, report_success
from fastapi import FastAPI
from rq import Queue, Retry
from redis import Redis

# Tell RQ what Redis connection to use
redis_conn = Redis()
q = Queue('messageQueue', connection=redis_conn) 

description = """
This API helps you do awesome stuff. 🚀

API that passes messages to a queue and a Python worker that works against the messages
"""

app = FastAPI(title="RQ with FastAPI",
    description=description,
    version="0.0.1")

@app.get('/')
def root():
    return { 'status': 'FastAPI is running' }

@app.post('/send')
def send_message(msg:str):
    job = q.enqueue(process_message, msg, retry=Retry(max=3))
    return { 'status': f'Job {job.id} is enqueued' }