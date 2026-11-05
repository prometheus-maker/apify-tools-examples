import os
from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_TOKEN"])
run = client.actor("prometheus-maker/image-to-text-ocr").call(run_input={
    "imageUrls": [{"url": "https://tesseract-ocr.github.io/tessdoc/images/eurotext.png"}],
    "languages": ["eng", "deu"],
})
for item in client.dataset(run.default_dataset_id).iterate_items():
    print(item["confidence"], item["text"][:200])
