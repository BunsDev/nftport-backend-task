import requests

HEADERS = {
    "Content-Type": "application/json",
    "Accept": "application/json"
}
payload = {
    "contract_id": "0xbc4ca0eda7647a8ab7c2061c2e118a18a936f13d",
    "token_id": "31"
}
result = requests.post("http://localhost:3000/get-token-uri", headers=HEADERS, json=payload)
result_json = result.json()
print(f"Got NFT tokenUri: {result_json}")
