import os
from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_TOKEN"])
run = client.actor("prometheus-maker/pdf-document-to-markdown").call(run_input={
    "startUrls": [{"url": "https://arxiv.org/pdf/1706.03762"}],
    "chunkSize": 1500,
})
for item in client.dataset(run.default_dataset_id).iterate_items():
    print(item["pageCount"], "pages,", len(item["chunks"]), "chunks")
    print(item["markdown"][:300])
