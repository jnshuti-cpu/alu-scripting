# api_advanced

Practice with the Reddit API using Python 3 and the `requests` module.

- `0-subs.py`: `number_of_subscribers(subreddit)` returns the subscriber count, 0 if invalid
- `1-top_ten.py`: `top_ten(subreddit)` prints the first 10 hot post titles, `None` if invalid
- `2-recurse.py`: `recurse(subreddit, hot_list=None, after=None)` recursively returns all hot titles, `None` if invalid
- `3-count.py`: `count_words(subreddit, word_list)` recursively counts keywords in hot titles and prints them sorted

All requests set a custom User-Agent and do not follow redirects.
