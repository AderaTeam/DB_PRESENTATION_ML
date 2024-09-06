from typing import Any
from models.generate_image_body_models import GenerateImageBody


def get_propmt_params(data: GenerateImageBody) -> dict[str, Any]:
    params = {
        "type": "GENERATE",
        "numImages": data.num_of_images,
        "width": data.width,
        "height": data.height,
        "generateParams": {
            "query": f"{data.text}"
        }
    }
    return params