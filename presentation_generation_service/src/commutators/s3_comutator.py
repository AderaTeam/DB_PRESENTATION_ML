
from typing import Any
from PIL import Image
from io import BytesIO
from constants import IMAGE_BUCKET_NAME, S3_CLIENT
from uuid import uuid4


def push_imgs_to_s3(fn: str):
    with open(fn, "rb") as f:
        S3_CLIENT.upload_fileobj(f, IMAGE_BUCKET_NAME, fn)
