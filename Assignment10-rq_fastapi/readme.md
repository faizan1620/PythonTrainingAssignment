# FastAPI with rq worker

A complete example of a rq worker and fastapi. API that passes messages to a queue and a Python worker that works against the messages.


#### Pre Requirements

 - Python3

 - pip 

 - Redis


### SETUP

1. Create a virtual env in python

    ```
    python -m venv /path/to/new/virtual/environment
    ```

2. Activate that virtual environment

    ```
    source /path_to_new_virtual_environment/bin/activate
    ```

3. Now run command to install required libraries

    ```
    pip install -r requirements.txt
    ```

### Run fastAPI server

To start fastAPI server, run the command
```
uvicorn main:app
```

Now, open the url:
```
localhost:8000/docs
```

When you hit the send api by passing **msg** as request body, the message will be enqueued to rq.

TO view/process those enqueued message, start the rq worker by using command:

```
rq worker messageQueue
```

