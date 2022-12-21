import requests
import pytest

@pytest.mark.parametrize("image_path", ['0_frog.png', '1_truck.png', '2_truck.png', '3_deer.png', '4_automobile.png', '5_automobile.png', '6_bird.png', '7_horse.png', '8_ship.png', '9_cat.png'])
def test_api(address, modelName, image_path):
    print("testing:", image_path)

    res = requests.post("http://"+address+":8080/predictions/"+modelName, files={'data': open("test_serve/"+image_path, 'rb')})
    res = res.json()

    assert max(res, key=res.get) == image_path.split('.')[0].split('_')[1]
