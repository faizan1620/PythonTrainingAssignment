# STUDENT MANAGEMENT SYSTEM (CRUD in FastAPI) using alembic migration

A complete example of a "CRUD" operation for Student Management System in which Student can opt any book also.

In this example:

- How to create CRUD endpoint.
- How to use [SqlAlchemy ORM](https://fastapi.tiangolo.com/tutorial/sql-databases/) with alembic migration
- How to document API with Swagger-UI.


## Overview


#### Pre Requirements

 - Python3

 - pip 

 - PostgreSQL database

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

4. Setup Postgresql database in your system and create a database

5. Create a .env file at root folder and provide the values:

    ```
    DB_USER=<Database_UserName>
    DB_PASSWORD=<Database_Password>
    DB_SERVER=<Database_Server>
    DB_Name=<DB_Name>

    ```

6. Now start the server by running the command:

    ```
    uvicorn main:app
    ```

    Now FastAPI server got started

5. Use this URL to open swagger-UI inorder to test the endpoints

    ```
     localhost:8000/docs
    ```

    You can also use Postman to test the routes/endpoints

### Endpoints 

|HTTP Method|URL|Description|
|---|---|---|
|`GET`|http://localhost:8000/ | Root page |
|`GET`|http://localhost:8000/student | Get all the student details |
|`GET`|http://localhost:8000/student/{id} | Get specific student details |
|`POST`|http://localhost:8000/student | Create a new student with details |
|`PUT`|http://localhost:8000/student/{id} | Update any specific student details |
|`DELETE`|http://localhost:8000/student/{id} | Delete any specific student details |
|`GET`|http://localhost:8000/book | Get all the book details |
|`GET`|http://localhost:8000/book/{id} | Get specific book details |
|`GET`|http://localhost:8000/book/{s_id} | Get book details for any specific student |
|`POST`|http://localhost:8000/book | Create a new book with details |
|`PUT`|http://localhost:8000/book/{id} | Update any specific book details |
|`DELETE`|http://localhost:8000/book/{id} | Delete any specific book details |

### Test

You can run the test cases also using pytest using command:

```
python3 -m pytest
```


