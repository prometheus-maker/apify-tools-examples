import os
from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_TOKEN"])
run = client.actor("prometheus-maker/website-screenshot").call(run_input={
    "urls": ["https://www.python.org", "https://example.com"],
    "fullPage": True,
})
for item in client.dataset(run.default_dataset_id).iterate_items():
    print(item["status"], item["url"], item.get("screenshotUrl"))
