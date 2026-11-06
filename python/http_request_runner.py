import os
from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_TOKEN"])
run = client.actor("prometheus-maker/http-request-runner").call(run_input={
    "requests": [
        {"url": "https://jsonplaceholder.typicode.com/posts/1", "lookupKey": "get-example"},
        {"url": "https://jsonplaceholder.typicode.com/posts", "method": "POST",
         "json": {"title": "Hello", "body": "From Apify", "userId": 1}, "lookupKey": "post-example"},
    ],
})
for item in client.dataset(run.default_dataset_id).iterate_items():
    print(item["lookupKey"], item["statusCode"], item["durationMs"], "ms")
