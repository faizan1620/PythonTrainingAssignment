# CELERY with FastAPI

Celery is a task queue with focus on real-time processing, while also supporting task scheduling.

## Overview

A complete example of a celery task queue to execute tasks using fastAPI

#### Pre Requirements

 - Python3

 - pip 

 - Celery

### SETUP

1. Create a virtual env in python

    ```
    python -m venv /path/to/new/virtual/environment
    ```

2. Activate that virtual environment

    ```
    source /path_to_new_virtual_environment/bin/activate
    ```

3. Install required packages using command:

    ```
    $ pip install -r requirements.txt
    ```

4. Now start the server by running the command:

    ```
    uvicorn main:app
    ```

    Now FastAPI server got started

5. Use this URL to open swagger-UI inorder to test the endpoints

    ```
     localhost:8000/docs
    ```

    You can also use Postman to test the routes/endpoints

6. Also use this url for starting celery worker

    ```
    celery -A modules.task.app worker --loglevel=info
    ```

### Endpoints 

|HTTP Method|URL|Description|
|---|---|---|
|`GET`|http://localhost:8000/ | Root page |
|`GET`|http://localhost:8000/start | To put a task in celery queue and get the id and the status of the task |
|`GET`|http://localhost:8000/status | Get the status of the task based on task_id |



