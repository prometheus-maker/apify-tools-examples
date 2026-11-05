import os
from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_TOKEN"])
run = client.actor("prometheus-maker/website-seo-audit").call(run_input={
    "startUrls": ["https://books.toscrape.com"],
    "maxPages": 10,
})
for item in client.dataset(run.default_dataset_id).iterate_items():
    if item["type"] == "page":
        print(item["score"], item["url"], [i["id"] for i in item["issues"]][:3])
    else:  # one site-summary per site
        print("site", item["site"], "average", item["averageScore"], "broken links", item["brokenLinkCount"])
