import os
from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_TOKEN"])
run = client.actor("prometheus-maker/bulk-file-downloader").call(run_input={
    "urls": ["https://www.w3.org/WAI/ER/tests/xhtml/testfiles/resources/pdf/dummy.pdf",
             "https://www.python.org/static/img/python-logo.png"],
})
for item in client.dataset(run.default_dataset_id).iterate_items():
    print(item["status"], item["fileName"], item["sizeBytes"], item["downloadUrl"])
