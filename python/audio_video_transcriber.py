import os
from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_TOKEN"])
run = client.actor("prometheus-maker/audio-video-transcriber").call(run_input={
    "urls": ["https://archive.org/download/art_of_war_librivox/art_of_war_01-02_sun_tzu.mp3"],
    "model": "base",
    "maxMinutesPerFile": 3,
})
for item in client.dataset(run.default_dataset_id).iterate_items():
    print(item["status"], item["minutesCharged"], "min:", item["text"][:200])
