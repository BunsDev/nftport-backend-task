# NFTPort Backend Test Assignment

### Getting NFTs

Use this [API endpoint](https://docs.nftport.xyz/docs/nftport/b3A6MjAzNDUzNTQ-retrieve-contract-nf-ts)
to fetch all contract addresses and token ids.

### Web3 gateway

Connects to the EVM compatible blockchain and fetches either tokenUri() or uri()
value from a given smart contract. Example usage in `web3_example.py`

Deploy web3 gateway:

```
cd web3_gateway
docker-compose up
```

Run example:

```
conda env create -f environment.yml
conda activate nftport-backend-task
python web3_example.py
```

Or just implement the equivalent API call in your language. 
