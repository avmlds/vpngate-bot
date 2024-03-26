import time
from typing import Callable

import requests

from vpngate_bot.constants import SCORE

LAST_FETCHED = "last_used"
DATA_KEY = "data"
SECONDS_IN_HOUR = 60 * 60


def cached(keep_alive: int = SECONDS_IN_HOUR * 2, memo={}):
    def wrapper_func(func: Callable):
        def wrapped(*args, **kwargs):
            if not memo.get(LAST_FETCHED) or (
                (time.time() - memo[LAST_FETCHED]) >= keep_alive
            ):
                memo[DATA_KEY] = func(*args, **kwargs)
                memo[LAST_FETCHED] = time.time()
            return memo[DATA_KEY]

        return wrapped

    return wrapper_func


@cached()
def get_vpngate_csv():
    """Get CSV and fetch data."""
    response = requests.get("http://www.vpngate.net/api/iphone/")
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
