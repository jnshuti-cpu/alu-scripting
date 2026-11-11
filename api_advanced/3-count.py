#!/usr/bin/python3
"""Module that recursively counts keywords in the titles of hot posts."""
import requests


def count_words(subreddit, word_list, after=None, counts=None):
    """Print a sorted count of keywords found in hot post titles.

    Case-insensitive; whole words only (split on spaces). Sorted by count
    descending, then alphabetically. Prints nothing if the subreddit is
    invalid or no keyword matches.
    """
    if counts is None:
        counts = {}
    if not subreddit or not isinstance(subreddit, str):
        return
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "linux:alu-scripting.api_advanced:v1.0.0"}
    params = {"limit": 100}
    if after:
        params["after"] = after
    try:
        res = requests.get(url, headers=headers, params=params,
                           allow_redirects=False, timeout=10)
        if res.status_code != 200:
            return
        data = res.json().get("data", {})
    except (requests.RequestException, ValueError):
        return

    for post in data.get("children", []):
        title = post.get("data", {}).get("title", "")
        for token in title.lower().split():
            counts[token] = counts.get(token, 0) + 1

    after = data.get("after")
    if after:
        return count_words(subreddit, word_list, after, counts)

    totals = {}
    for word in word_list:
        word = word.lower()
        if counts.get(word):
            totals[word] = totals.get(word, 0) + counts[word]
    for word, num in sorted(totals.items(), key=lambda kv: (-kv[1], kv[0])):
        print("{}: {}".format(word, num))
