import json
import os

OUTPUT_PATH = "data/rarible"


def main(output_path=OUTPUT_PATH, contract_address=None):
    nfts = _get_all_nfts(output_path, contract_address)
    print("nfts len:", len(nfts))
    _save_nfts(nfts, contract_address)
    return nfts


def _get_all_nfts(output_path=OUTPUT_PATH, contract_address=None):
    result = []
    for dir_path in os.listdir(output_path):
        dir_path = os.path.join(output_path, dir_path)
        if not contract_address \
                or (contract_address and dir_path.endswith(contract_address)):
            print("getting NFTs from path:", dir_path)
            result += _get_nfts(dir_path)
    return result


def _get_nfts(dir_path: str):
    result = []
    for file_path in os.listdir(dir_path):
        file_path = os.path.join(dir_path, file_path)
        result += _read_nfts_from_disk(file_path)
    return result


def _read_nfts_from_disk(file_path: str):
    raw_data = _read_file(file_path)
    result = []
    for item in raw_data["items"]:
        result.append({
            "address": item["contract"],
            "token_id": item["tokenId"]
        })
    return result


def _read_file(file_path: str):
    with open(file_path) as f:
        return json.loads(f.read())


def _save_nfts(nfts, contract_address):
    file_path = f"rarible_{contract_address}.json"
    file_path = os.path.join(OUTPUT_PATH, file_path)
    print("Saving nfts to:", file_path)
    with open(file_path, "w") as f:
        f.write(json.dumps(nfts))
