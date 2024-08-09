import simple_script
import time
import requests

result_of_random = simple_script.add_vars()
print(result_of_random)

def test_is_int():
    is_int = isinstance(result_of_random, int)
    assert is_int is True

def test_lower_than_13():
    time.sleep(10)
    assert  result_of_random < 13

x = requests.get('https://rickandmortyapi.com/api/episode/10,28')
print(x.text)