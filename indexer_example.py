from indexer.rarible_indexer import Indexer

"""
Install required dependencies in any way you like, see the dependencies in 
environment.yml
"""

indexer = Indexer()
tokens = indexer.execute(
    contract_address="0xbc4ca0eda7647a8ab7c2061c2e118a18a936f13d"
)
print(f"Got tokens: {len(tokens)}")
