#!/usr/bin/python3
"""Module that queries the Reddit API for a subreddit's subscriber count."""
import requests


def number_of_subscribers(subreddit):
    """Return the total number of subscribers for a subreddit.

    Returns 0 if the subreddit is invalid.
    """
    if not subreddit or not isinstance(subreddit, str):
        return 0
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "linux:alu-scripting.api_advanced:v1.0.0"}
    try:
        res = requests.get(url, headers=headers, allow_redirects=False,
                           timeout=10)
        if res.status_code != 200:
            return 0
        return res.json().get("data", {}).get("subscribers", 0)
    except (requests.RequestException, ValueError):
        return 0
