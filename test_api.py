from app import app
from flask import json

def test_in_mkad():        
    data = {'address': "москва, красная площадь"}
    response = app.test_client().get(
        '/v1/',
        query_string = data
    )

    data = json.loads(response.get_data(as_text=True))

    assert response.status_code == 200
    assert data['distance'] == 0


def test_close_out_mkad():        
    data = {'address': "Реутовская улица, 6"
                "Балашиха, Московская область"}
    response = app.test_client().get(
        '/v1/',
        query_string = data
    )

    data = json.loads(response.get_data(as_text=True))

    assert response.status_code == 200
    assert 0.4 <= data['distance'] <= 0.9



def test_close_in_mkad():        
    data = {'address': "улица Маршала Прошлякова, 26к3с1 Москва"}
    response = app.test_client().get(
        '/v1/',
        query_string = data
    )

    data = json.loads(response.get_data(as_text=True))

    assert response.status_code == 200
    assert data['distance'] == 0


def test_out_mkad():        
    data = {'address': "Нижний Новгород, Пискунова 16"}
    response = app.test_client().get(
        '/v1/',
        query_string = data
    )

    data = json.loads(response.get_data(as_text=True))

    assert response.status_code == 200
    assert 387 <= data['distance'] <= 390


def test_bad_requst():
    data = {'address': "Нdfs6 sdfx"}
    response = app.test_client().get(
        '/v1/',
        query_string = data
    )

    data = json.loads(response.get_data(as_text=True))

    assert response.status_code == 400
    assert "error" in data