import requests
import json
from helpers.constants import API_KEY, BASE_URL
import random
obj = {}

randomPage = random.randint(10,400)


def test_GET_top_rated_movies():
    params = {'api_key': API_KEY}
    response = requests.get(BASE_URL + '/movie/top_rated', params=params)
    assert response.status_code == 200
    print(response.status_code)
    print(response.text)

def test_GET_incorrect_api_key_401():
    params = {'api_key': 'wrong_key'}
    response = requests.get(BASE_URL + '/movie/top_rated', params=params)
    assert response.status_code == 401

def test_GET_Should_not_top_rated_movies_with_page_0():
    params = {
        'api_key': API_KEY,
        'page': 0
        }
    response = requests.get(BASE_URL + '/movie/top_rated', params=params)
    assert response.status_code == 422

def test_GET_Should_top_rated_movies_with_max_page():
    params = {
        'api_key': API_KEY,
        'page': 500
        }
    response = requests.get(BASE_URL + '/movie/top_rated', params=params)
    assert response.status_code == 200

def test_GET_Should_top_rated_movies_with_random_page_between_1_500():
    params = {
        'api_key': API_KEY,
        'page': randomPage
        }
    response = requests.get(BASE_URL + '/movie/top_rated', params=params)
    assert response.status_code == 200
    data = json.loads(response.content)
    assert data["page"] == randomPage
    obj["movieId"] = data["results"][0]["id"]
