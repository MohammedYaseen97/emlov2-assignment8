import requests

import torch
import numpy as np

from PIL import Image

from captum.attr import visualization as viz

from torchvision.transforms import transforms
from pl_bolts.transforms.dataset_normalizations import cifar10_normalization

import matplotlib.pyplot as plt

def test_captum(address, modelName):
    img_path = 'test_serve/9_cat.png'

    print("testing:", img_path)

    res = requests.post("http://"+address+":8080/explanations/"+modelName, files={'data': open(img_path, 'rb')})
    ig = res.json()

    inp_image = Image.open(img_path)
    to_tensor = transforms.Compose(
            [transforms.ToTensor(), cifar10_normalization()]
            )
    inp_image = to_tensor(inp_image)

    inp_image = inp_image.numpy()
    attributions = np.array(ig)

    inp_image, attributions = inp_image.transpose(1, 2, 0), attributions.transpose(1, 2, 0)

    assert inp_image.shape == attributions.shape
