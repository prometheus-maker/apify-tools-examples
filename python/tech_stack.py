import os
from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_TOKEN"])
run = client.actor("prometheus-maker/website-tech-stack-detector").call(run_input={
    "urls": ["wordpress.org", "python.org", "react.dev"],
})
for item in client.dataset(run.default_dataset_id).iterate_items():
    print(item["domain"], "->", ", ".join(t["name"] for t in item["technologies"]))
