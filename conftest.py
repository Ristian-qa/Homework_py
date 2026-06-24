import pytest
import requests
from config import BASE_URL, HEADERS


@pytest.fixture
def api_url():
    return BASE_URL


@pytest.fixture
def headers():
    return HEADERS


@pytest.fixture
def create_test_project(api_url, headers):
    created_projects = []

    def _create_project(title="Test Project"):
        payload = {"title": title}
        response = requests.post(f"{api_url}/projects", json=payload,
                                 headers=headers)

        if response.status_code == 201:
            project_id = response.json().get("id")
            if project_id:
                created_projects.append(project_id)
                return project_id, response

        return None, response

    yield _create_project

    for project_id in created_projects:
        requests.put(
            f"{api_url}/projects/{project_id}",
            json={"deleted": True},
            headers=headers
        )
