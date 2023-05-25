from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

requestBody = {
    "branch": "test_branch",
    "gender": "Unknown",
    "age": 25,
    "name": "test_name",
    "registration": 10,
}

updateRequestBody = {
    "branch": "updated_branch",
    "gender": "Unknown",
    "age": 30,
    "name": "updated_name",
    "registration": 10,
}


def test_get_student():
    response = client.get("/student")
    assert response.status_code == 200


def test_post_student():
    global id
    response = client.post("/student/", json=requestBody)
    id = response.json()["id"]
    assert response.status_code == 200
    assert response.json() == {
        "id": id,
        "branch": "test_branch",
        "gender": "Unknown",
        "age": 25,
        "name": "test_name",
        "registration": 10,
    }


def test_post_student_invalid_request_body():
    response = client.post("/student/", json={"test": "invalid body"})
    assert response.status_code == 422


def test_get_student_by_id():
    response = client.get(f"/student/{id}")
    assert response.status_code == 200
    assert response.json() == {
        "id": id,
        "branch": "test_branch",
        "gender": "Unknown",
        "age": 25,
        "name": "test_name",
        "registration": 10,
    }


def test_get_student_by_id_doesnot_exist():
    response = client.get("/student/1000")
    assert response.status_code == 404
    assert response.json() == {"detail": "Student with id: 1000 doesnot exist"}


def test_update_student_by_id():
    response = client.put(f"/student/{id}", json=updateRequestBody)
    assert response.status_code == 200
    assert response.json() == {
        "id": id,
        "branch": "updated_branch",
        "gender": "Unknown",
        "age": 30,
        "name": "updated_name",
        "registration": 10,
    }


def test_update_student_by_id_doesnot_exist():
    response = client.put("/student/100", json=updateRequestBody)
    assert response.status_code == 404
    assert response.json() == {"detail": "Student couldnot be updated with id: 100"}


def test_delete_student_by_id():
    response = client.delete(f"/student/{id}")
    assert response.status_code == 200
    assert response.json() == {
        "detail": f"Student with id: {id} deleted successfully!",
        "status": "Success",
    }


def test_delete_student_by_id_doesnot_exist():
    response = client.delete("/student/1000")
    assert response.status_code == 404
    assert response.json() == {"detail": "Student couldnot be deleted with id: 1000"}
