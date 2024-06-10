import requests
import allure
import json
import pytest


@pytest.mark.regression
def test_regress():
    print("This test case is in regression scope")


URL = "https://petstore.swagger.io/v2/"


@allure.title("Создаем питомца и получаем")
@pytest.mark.regresiion
def test_add_pet():
    payload = {
        "id": 0,
        "category": {
            "id": 0,
            "name": "cat"
        },
        "name": "Simba",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    }

    response = requests.post(
        url=f"{URL}pet",
        headers={"accept": "application/json",
                 "Content-Type": "application/json"},
        json=payload
    )

    assert response.status_code == 200

    pet_id = response.json()["id"]
    get_response = requests.get(
        url=f"{URL}pet/{pet_id}",
        headers={"accept": "application/json"}
    )

    assert get_response.status_code == 200
    print(pet_id)
    print(get_response.json())


@allure.title("Изменяем питомца")
def test_update_pet_put():
    payload = {
        "id": 0,
        "category": {
            "id": 0,
            "name": "cat"
        },
        "name": "Kot",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    }

    response = requests.post(
        url=f"{URL}pet",
        headers={"accept": "application/json",
                 "Content-Type": "application/json"},
        json=payload
    )
    pet_id = response.json()["id"]
    assert response.status_code == 200

    update_payload = {
        "id": pet_id,
        "category": {
            "id": 0,
            "name": "cat"
        },
        "name": "Bonya",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "Maine Coon"
            }
        ],
        "status": "available"
    }

    put_response = requests.put(
        url=f"{URL}pet",
        headers={"accept": "application/json",
                 "Content-Type": "application/json"},
        json=update_payload
    )
    assert put_response.status_code == 200

    get_response = requests.get(
        url=f"{URL}pet/{pet_id}",
        headers={"accept": "application/json"}
    )
    assert get_response.status_code == 200
    assert get_response.json()["name"] == "Bonya"
    print(get_response.json())


@allure.title("Удаляем питомца")
def test_delete_pet():
    payload = {
        "id": 0,
        "category": {
            "id": 0,
            "name": "dog"
        },
        "name": "Sharik",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    }
    response = requests.post(
        url=f"{URL}pet",
        headers={"accept": "application/json",
                 "Content-Type": "application/json"},
        json=payload
    )

    assert response.status_code == 200
    pet_id = response.json()["id"]

    delete_response = requests.delete(
        url=f"{URL}pet/{pet_id}",
        headers={"accept": "application/json"}
    )
    assert delete_response.status_code == 200

    get_response = requests.get(
        url=f"{URL}pet/{pet_id}",
        headers={"accept": "application/json"}
    )

    assert get_response.status_code == 404


@allure.title("Выборка по статусу")
def test_pet_find_by_status():
    get_response = requests.get(
        url=f"{URL}pet/findByStatus",
        params={"status": "available"},
        headers={"accept": "application/json"}
    )
    assert get_response.status_code == 200
    print()
    print(get_response.url)


@allure.title("Изменяем статус")
def test_update_pet_status():
    payload = {
        "id": 0,
        "category": {
            "id": 0,
            "name": "cat"
        },
        "name": "Kotik",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    }

    response = requests.post(
        url=f"{URL}pet",
        headers={"accept": "application/json",
                 "Content-Type": "application/json"},
        json=payload
    )
    pet_id = response.json()["id"]
    assert response.status_code == 200

    post_response = requests.post(
        url=f"{URL}pet/{pet_id}",
        headers={"accept": "application/json",
                 "Content-Type": "application/x-www-form-urlencoded"},
        params={"name": "Kotik",
                "status": "sold"}
    )
    assert post_response.status_code == 200

    get_response = requests.get(
        url=f"{URL}pet/{pet_id}",
        headers={"accept": "application/json"}
    )

    print(get_response.json())


@pytest.mark.skip(reason="smth goes wrong")
@allure.title("Загружаем фото питомца")
def test_upload_image():
    payload = {
        "id": 0,
        "category": {
            "id": 0,
            "name": "cat"
        },
        "name": "Myrka",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    }

    response = requests.post(
        url=f"{URL}pet",
        headers={"accept": "application/json",
                 "Content-Type": "application/json"},
        json=payload
    )
    pet_id = response.json()["id"]
    assert response.status_code == 200

    post_response = requests.post(
        url=f"{URL}pet/{pet_id}/uploadImage",
        headers={"accept": "application/json"},
        files={"file": open("photo_cat.jpg", "rb")}

    )

    assert post_response.status_code == 200




"""
pytest .\task1\test_1.py --alluredir=.\task1\reports
allure serve .\task1\reports 
python -m pytest .\task1\test_1.py -m "regression"


"""
