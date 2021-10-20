import json
import os
import time

import requests
from urllib.error import HTTPError

from indexer import combine_tokens

BASE_URL = "https://ethereum-api.rarible.org/v0.1/nft/items/byCollection"
PAGE_SIZE = 1000
OUTPUT_PATH = "data/rarible"
SLEEP_ON_ERROR = 3


class Indexer:

    def execute(self, contract_address: str, current_page: int = 0):
        try:
            self._execute(contract_address, i=current_page)
        except:
            pass
        return combine_tokens.main(OUTPUT_PATH, contract_address)

    def _execute(self, contract_address, i=0):
        continuation = None
        if i > 0:
            continuation = _get_continuation(contract_address, i)
            print("got continuation:", continuation)
        while True:
            try:
                start = time.time()
                status_code, json_data = _make_request(contract_address, continuation)
                print("query:", i)
                print("  duration:", time.time() - start)
                print("  status_code:", status_code)
                print("  items len:", len(json_data["items"]))
                _save(contract_address, json_data, i)
                continuation = json_data["continuation"]
                i += 1
            except Exception as e:
                error: HTTPError = e
                print("error:", error)
                if error.response.status_code not in [200]:
                    time.sleep(3)


def _get_continuation(contract_address, i):
    with open(_get_file_name(contract_address, i)) as f:
        data = json.loads(f.read())
        return data["continuation"]


def _save(contract_address, json_data, i):
    file_path = _get_file_name(contract_address, i)
    with open(file_path, "w") as f:
        f.write(json.dumps(json_data))


def _get_file_name(contract_address, i):
    file_path = os.path.join(OUTPUT_PATH, contract_address)
    os.makedirs(file_path, exist_ok=True)
    return os.path.join(file_path, f"page_{i}.json")


def _make_request(contract_address, continuation=None):
    query = {
        "collection": contract_address,
        "size": PAGE_SIZE,
        "continuation": continuation
    }
    result = requests.get(BASE_URL, params=query)
    if result.status_code == 200:
        return result.status_code, result.json()
