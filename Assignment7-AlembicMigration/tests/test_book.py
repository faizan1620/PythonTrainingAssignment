from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

requestBody = {"title": "test_book", "department": "test_department"}

updateRequestBody = {"title": "updated_book", "department": "updated_department"}


# Creating a student just for using that id in book
def test_post_student():
    global student_id
    response = client.post(
        "/student/",
        json={
            "branch": "test_branch",
            "gender": "Unknown",
            "age": 25,
            "name": "test_name",
            "registration": 10,
        },
    )
    student_id = response.json()["id"]


def test_get_book():
    response = client.get("/book")
    assert response.status_code == 200


def test_post_book():
    global id
    response = client.post(
        "/book/", json=requestBody, params={"student_id": student_id}
    )
    id = response.json()["id"]
    assert response.status_code == 200
    assert response.json() == {
        "id": id,
        "book_id": student_id,
        "title": "test_book",
        "department": "test_department",
    }


def test_post_book_invalid_request_body():
    response = client.post("/book/", json={"test": "invalid body"})
    assert response.status_code == 422


def test_get_book_by_id():
    response = client.get(f"/book/{id}")
    assert response.status_code == 200
    print(response.json())
    assert response.json() == {
        "id": id,
        "book_id": student_id,
        "title": "test_book",
        "department": "test_department",
    }


def test_get_book_by_id_doesnot_exist():
    response = client.get("/book/1000")
    assert response.status_code == 404
    assert response.json() == {"detail": "Book with id: 1000 doesnot exist"}


def test_update_book_by_id():
    response = client.put(f"/book/{id}", json=updateRequestBody)
    assert response.status_code == 200
    assert response.json() == {
        "title": "updated_book",
        "department": "updated_department",
    }


def test_update_book_by_id_doesnot_exist():
    response = client.put("/book/100", json=updateRequestBody)
    assert response.status_code == 404
    assert response.json() == {"detail": "Book couldnot be updated with id: 100"}


def test_delete_book_by_id():
    response = client.delete(f"/book/{id}")
    assert response.status_code == 200
    assert response.json() == {
        "detail": f"Book with id: {id} deleted successfully!",
        "status": "Success",
    }


def test_delete_book_by_id_doesnot_exist():
    response = client.delete("/book/1000")
    assert response.status_code == 404
    assert response.json() == {"detail": "Book couldnot be deleted with id: 1000"}
