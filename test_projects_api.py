import requests
from config import BASE_URL


def _extract_project(data):
    if "id" in data and "title" in data:
        return data
    if "data" in data and isinstance(data["data"], dict):
        return data["data"]
    if "project" in data:
        return data["project"]
    return data


# ПОЗИТИВНЫЕ ТЕСТЫ

# Создание проекта с корректными данными
def test_create_project_success(api_url, headers):
    payload = {"title": "Project from test"}
    response = requests.post(f"{api_url}/projects", json=payload,
                             headers=headers)

    assert response.status_code == 201

    project = _extract_project(response.json())
    assert "id" in project

    project_id = project.get("id")
    if project_id:
        requests.put(
            f"{api_url}/projects/{project_id}",
            json={"deleted": True},
            headers=headers
        )


# Получение существующего проекта по ID
def test_get_project_success(api_url, headers, create_test_project):
    project_id, _ = create_test_project("Project for GET test")
    assert project_id

    response = requests.get(f"{api_url}/projects/{project_id}",
                            headers=headers)
    assert response.status_code == 200

    project = _extract_project(response.json())
    assert project.get("id") == project_id


# Обновление названия существующего проекта
def test_update_project_success(api_url, headers, create_test_project):
    project_id, _ = create_test_project("Project for UPDATE test")
    assert project_id

    new_title = "Updated project name"
    update_response = requests.put(
        f"{api_url}/projects/{project_id}",
        json={"title": new_title},
        headers=headers
    )
    assert update_response.status_code == 200

    get_response = requests.get(f"{api_url}/projects/{project_id}",
                                headers=headers)
    assert get_response.status_code == 200

    project = _extract_project(get_response.json())
    actual_title = project.get("title") or project.get("name")
    assert actual_title == new_title


# НЕГАТИВНЫЕ ТЕСТЫ

# Создание проекта с пустым названием
def test_create_project_empty_title(api_url, headers):
    response = requests.post(
        f"{api_url}/projects",
        json={"title": ""},
        headers=headers
    )
    assert response.status_code == 400
    assert "error" in response.json()


# Запрос проекта по несуществующему ID
def test_get_project_not_found(api_url, headers):
    fake_id = "00000000-0000-0000-0000-000000000000"
    response = requests.get(f"{api_url}/projects/{fake_id}", headers=headers)
    assert response.status_code == 404


# Обновление проекта по несуществующему ID
def test_update_project_not_found(api_url, headers):
    fake_id = "00000000-0000-0000-0000-000000000000"
    response = requests.put(
        f"{api_url}/projects/{fake_id}",
        json={"title": "New title"},
        headers=headers
    )
    assert response.status_code == 404


# Запрос на создание проекта без токена авторизации
def test_create_project_unauthorized():
    url = f"{BASE_URL}/projects"
    headers_no_auth = {"Content-Type": "application/json"}
    payload = {"title": "No auth test"}

    response = requests.post(url, json=payload, headers=headers_no_auth)
    assert response.status_code == 401
