import time
from typing import Callable

import requests

from vpngate_bot.constants import SCORE

LAST_FETCHED = "last_used"
DATA_KEY = "data"
SECONDS_IN_HOUR = 60 * 60


def cached(keep_alive: int = SECONDS_IN_HOUR * 4, memo={}):
    def wrapper_func(func: Callable):
        def wrapped(*args, **kwargs):
            if not memo.get(LAST_FETCHED) or (
                (time.time() - memo[LAST_FETCHED]) >= keep_alive
            ):
                try:
                    memo[DATA_KEY] = func(*args, **kwargs)
                    memo[LAST_FETCHED] = time.time()
                except requests.ConnectionError as e:
                    print(f"Unsuccessful request attempt, reason: {e}")
                    if memo.get(DATA_KEY):
                        memo[LAST_FETCHED] = time.time() + SECONDS_IN_HOUR * 2
                    else:
                        raise
            return memo[DATA_KEY]
        return wrapped
    return wrapper_func


@cached()
def get_vpngate_csv():
    """Get CSV and fetch data."""
    response = requests.get(
        "http://www.vpngate.net/api/iphone/",
        headers={
            "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:124.0) Gecko/20100101 Firefox/124.0",
            "Accept": "text/html,application/xml;q=0.9",
            "Accept-Language": "en-US,en;q=0.5",
            "Accept-Encoding": "gzip, deflate",
            "Connection": "keep-alive",
        },
        timeout=200
    )
    response.raise_for_status()
    lines = response.text.splitlines()
    data = []
    headers = lines[1].split(",")
    headers[0] = headers[0].replace("#", "")

    for line in lines[2:]:
        content = line.split(",")
        if len(headers) != len(content):
            print(f"Invalid line {line}")
            continue
        line_dict = {}
        for h, c in zip(headers, content):
            line_dict[h] = c
        data.append(line_dict)
    return sorted(data, key=lambda x: x[SCORE], reverse=True)
