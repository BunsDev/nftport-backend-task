const ethers = require('ethers');

// Free alchemy key
const url = "https://eth-mainnet.alchemyapi.io/v2/XQDZ-hFcsUFlbHpFsb-NaFJzugCQK8Og";
const provider = new ethers.providers.JsonRpcProvider(url);

const express = require('express');
const bodyParser = require('body-parser');

const app = express();
app.use(bodyParser.urlencoded({extended: true}));
app.use(bodyParser.json());
app.use(bodyParser.raw());

const abiErc721 = [
  "function name() view returns (string)",
  "function symbol() view returns (string)",
  "function tokenURI(uint256 tokenId) external view returns (string memory)"
];


const abiErc1155 = [
  "function name() view returns (string)",
  "function symbol() view returns (string)",
  "function uri(uint256 tokenId) external view returns (string memory)"
];

const getTokenURI = async function (contract_id, token_id) {
  // The Contract object
  const daiContract = new ethers.Contract(contract_id, abiErc721, provider);
  const token_uri = await daiContract.tokenURI(token_id)
  return {token_uri: token_uri}
}

const getTokenURIErc1155 = async function (contract_id, token_id) {
  // The Contract object
  const daiContract = new ethers.Contract(contract_id, abiErc1155, provider);
  let token_uri = await daiContract.uri(token_id)
  token_uri = token_uri.replace("0x{id}", token_id)
  return {token_uri: token_uri}
}

app.post('/get-token-uri', async (req, res) => {
  try {
    console.log('/get-token-uri -> req:', req.body);
    res.setHeader('Content-Type', 'application/json');
    const token_uri = await getTokenURI(req.body.contract_id, req.body.token_id)
    console.log('/get-token-uri -> res:', token_uri)
    res.end(JSON.stringify(token_uri));
  } catch (e) {
    console.log('/get-token-uri -> res:', e)
    res.status(400).json(e["reason"])
  }
});

app.post('/get-token-uri-erc1155', async (req, res) => {
  try {
    console.log('/get-token-uri-erc1155 -> req:', req.body);
    res.setHeader('Content-Type', 'application/json');
    const token_uri = await getTokenURIErc1155(req.body.contract_id, req.body.token_id)
    console.log('/get-token-uri-erc1155 -> res:', token_uri)
    res.end(JSON.stringify(token_uri));
  } catch (e) {
    console.log('/get-token-uri -> res:', e)
    res.status(400).json(e["reason"])
  }
});

app.listen(3000, () => console.log(`Started server at http://localhost:3000`));