import os
from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_TOKEN"])
run = client.actor("prometheus-maker/website-to-markdown-crawler").call(run_input={
    "startUrls": ["https://docs.python.org/3/tutorial/"],
    "maxPages": 5,
    "chunkSize": 2000,  # each item also gets "chunks", ready for embeddings
})
for item in client.dataset(run.default_dataset_id).iterate_items():
    print(item["type"], item["url"], item["wordCount"], "words,", len(item.get("chunks", [])), "chunks")
