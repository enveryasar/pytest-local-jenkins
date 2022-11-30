import requests
from helpers.constants import API_KEY

BASE_URL = 'https://api.themoviedb.org/3'


def test_movie():
    params = {'api_key': API_KEY}
    response = requests.get(BASE_URL + '/movie/top_rated', params=params)
    assert response.status_code == 200
    print(response.status_code)
    print(response.text)