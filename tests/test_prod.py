from fastapi.testclient import TestClient
from fast_api.main import api
import pytest   # noqa, flake8 issue

client = TestClient(api)


def test_product_getall():
    response = client.get('/products')
    assert response.status_code == 200
    assert len(response.json()) == 2


def test_product_getone():
    response = client.get('/products/1')
    assert response.status_code == 200
    assert response.json().get('name') == 'kebab'


def test_product_insert():
    new_product = {
        'id': 3,
        'name': 'name panino 3',
        'description': 'sarhwerhw54e',
        'price': 4,
        'avaible': True
    }
    response = client.post('/products/', json=new_product)
    assert response.status_code == 200
    assert response.json() == new_product


def test_product_delete():
    product_id = 1
    response = client.delete(f'/products/{product_id}')
    assert response.status_code == 200


def test_product_update():
    product_id = 1
    description = 'descrizione nuova'
    modify_product = {
        'id': product_id,
        'name': 'kebab',
        'description': description,
        'price': 4,
        'avaible': True
    }
    response = client.put(
        f'/products/{product_id}',
        json=modify_product
    )
    assert response.status_code == 200
