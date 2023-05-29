#!/usr/bin/python3

# Future import for type annotations
from __future__ import annotations

# Standard Library
import base64
import binascii
import tempfile
from typing import TYPE_CHECKING, List, Callable, Dict, Union

# Pip Install
from torch import zeros, uint8
from torchvision.transforms import Pad
from torchvision.io.image import read_image
from PIL import Image, UnidentifiedImageError
from torchvision.models.detection import fasterrcnn_resnet50_fpn_v2, FasterRCNN_ResNet50_FPN_V2_Weights


if TYPE_CHECKING:
    from torch import Tensor
    from torchvision.models.detection import FasterRCNN


def _apply_patch(im: Tensor, p: Tensor) -> Tensor:
    """Puts the patch in the top left corner of the image.
    :param im: The image to have a patch placed on
    :param p: The patch to apply onto the image. Must be smaller than the image
    :return: The Tensor object of the image
    """
    mask: Tensor = zeros(p.size(), dtype=uint8)
    # The list argument determines the padding from left, top, right, bottom
    mask = Pad([0, 0, im.size(2) - p.size(2), im.size(1) - p.size(1)], fill=1)(mask)
    p = Pad([0, 0, im.size(2) - p.size(2), im.size(1) - p.size(1)], fill=0)(p)
    return im * mask + p


# Load the model
weights: FasterRCNN_ResNet50_FPN_V2_Weights = FasterRCNN_ResNet50_FPN_V2_Weights.COCO_V1
preprocess: Callable[[Union[Image, Tensor]], Tensor] = weights.transforms()
model: FasterRCNN = fasterrcnn_resnet50_fpn_v2(weights=weights, box_score_thresh=0.9)
model.eval()

# Load the cat image
img: Tensor = preprocess(read_image('cat.jpg'))


# Load the patch from stdin
input_str: str = input()

# Try to decode the data as base64
try:
    input_data: bytes = base64.b64decode(input_str, validate=True)
except binascii.Error as be:
    print('Cat Hater: The data you sent me doesn\'t look like base64. Encode your patch with:\n\t$ base64 -i patch.jpg')
    print('Cat Hater: The full command may look like:\n\t$ base64 -i patch.jpg | nc [ip] [port]')
    exit(1)

# Open a temporary file and store that data into it
with tempfile.TemporaryFile() as fp:
    fp.write(input_data)
    fp.flush()

    # Now load it as a PIL image
    try:
        patch_image: Image = Image.open(fp, mode='r', formats=['JPEG', 'JPEG2000']).convert('RGB')
    except UnidentifiedImageError as uie:
        print('Cat Hater: I could not interpret your sent data as a valid image. '
              'Make sure it is a jpg you are sending me.')
        exit(1)
    except Exception as e:
        print('Cat Hater: I had an unexpected error. Please contact an admin for support if this problem persists.')
        exit(1)

    # Turn it into a tensor, now safe to destroy the temp file
    patch: Tensor = preprocess(patch_image)


# Apply the given patch
if patch.ndim != 3 or patch.size(1) > 100 or patch.size(2) > 100:
    raise ValueError('Cat Hater: Your patch is not valid. Please ensure that the patch is a JPG less than 100x100.')
else:
    img = _apply_patch(img, patch)

# Run the model against the patched image
predictions: List[Dict[str, Tensor]] = model([img])
labels: List[str] = [weights.meta["categories"][i] for i in predictions[0]["labels"]]
print(f'Cat Hater: I can see this \n\t{labels[0]}\nwith confidence\n\t{predictions[0]["scores"][0]}')

if 'cat' != labels[0]:
    with open('flag.txt') as f:
        print(f'Cat Hater: Thank goodness, no cats!\nCat Hater: Have a flag!\n\t{f.read()}')
else:
    print('Cat Hater: Eww! I hate cats!')
