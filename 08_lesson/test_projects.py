import uuid

from YougileApi import YougileApi


api = YougileApi("https://yougile.com/api-v2")


def create_test_project():
    title = "Autotest " + str(uuid.uuid4())

    response = api.create_project(title)

    assert response.status_code == 201

    project_id = response.json()["id"]

    return {
        "id": project_id,
        "title": title
    }


# POST /projects


def test_create_project_positive():
    title = "Autotest " + str(uuid.uuid4())

    response = api.create_project(title)

    assert response.status_code == 201

    body = response.json()

    assert body["id"] is not None

    project_id = body["id"]

    response = api.get_project(project_id)

    assert response.status_code == 200

    body = response.json()

    assert body["id"] == project_id
    assert body["title"] == title


def test_create_project_negative():
    response = api.create_project("")

    assert response.status_code >= 400

    body = response.json()

    assert "error" in body


# GET /projects/{id}


def test_get_project_positive():
    project = create_test_project()
    project_id = project["id"]

    response = api.get_project(project_id)

    assert response.status_code == 200

    body = response.json()

    assert body["id"] == project_id
    assert body["title"] == project["title"]


def test_get_project_negative():
    fake_id = str(uuid.uuid4())

    response = api.get_project(fake_id)

    assert response.status_code >= 400

    body = response.json()

    assert "error" in body


# PUT /projects/{id}


def test_update_project_positive():
    project = create_test_project()
    project_id = project["id"]

    new_title = "Updated " + str(uuid.uuid4())

    response = api.update_project(project_id, new_title)

    assert response.status_code == 200

    body = response.json()

    assert body["id"] == project_id

    response = api.get_project(project_id)

    assert response.status_code == 200

    body = response.json()

    assert body["title"] == new_title


def test_update_project_negative():
    fake_id = str(uuid.uuid4())

    response = api.update_project(
        fake_id,
        "Updated project"
    )

    assert response.status_code >= 400

    body = response.json()

    assert "error" in body
