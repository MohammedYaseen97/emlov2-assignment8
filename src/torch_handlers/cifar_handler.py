import torch
import torch.nn.functional as F

from ts.torch_handler.vision_handler import VisionHandler
from ts.utils.util import map_class_to_label

from torchvision.transforms import transforms
from pl_bolts.transforms.dataset_normalizations import cifar10_normalization

class ImageClassifier(VisionHandler):
    """
    ImageClassifier handler class. This handler takes an image
    and returns the name of object in that image.
    """

    topk = 5
    # Transforms copied from src/datamodules/cifar
    image_processing = transforms.Compose(
            [transforms.ToTensor(), cifar10_normalization()]
            )

    def set_max_result_classes(self, topk):
        self.topk = topk

    def get_max_result_classes(self):
        return self.topk

    def postprocess(self, data):
        ps = F.softmax(data, dim=-1)
        probs, classes = torch.topk(ps, self.topk, dim=1)
        probs = probs.tolist()
        classes = classes.tolist()
        return map_class_to_label(probs, self.mapping, classes)
