const request = require('request')
const IPFS = require('ipfs-http-client');
const ipfs = new IPFS({ host: 'ipfs.infura.io', port: 5001, protocol: 'https' });
const Web3 = require ('web3');
const  {IExec}   =  require ('iexec');

const eprovider = require('eth-provider')

const abi = require('./ABI.json');
const address = '0x97D92d73780dC73439d5f451768dDB5667DD36A6';

const createRequest = (input, callback) => {

//so what now
//
const web3 = new Web3(new Web3.providers.HttpProvider("https://kovan.infura.io/v3/86978d230e2744ab9b8d10e9f2ae655f"))
const web3contract  = new web3.eth.Contract(abi, address);


  networkVersion = "42";
  ethProvider =  eprovider("https://kovan.infura.io/v3/86978d230e2744ab9b8d10e9f2ae655f");


  console.log(ethProvider);

const iexec = new IExec({
  ethProvider: ethProvider,
  chainId: networkVersion, // id of the chain (42 for kovan)
});

const userAddress =  iexec.wallet.checkBalances().then(function(r){
  console.log('User address:', r);
});

// const balance =  iexec.wallet.checkBalances(ethAddress).then(function(r){
//   console.log('Nano RLC:', r.nRLC.toString());
//   console.log('Eth wei:', r.wei.toString());
// });


let a = web3contract.methods.getTaskUsrData(1).call().then(function(resp) {
   console.log(" works " + resp) // This will output "OK Computer"
});

console.log(input.hash);
//  input.data.coin
const validCID = 'QmT1e9gmutXPqNnNQhTX8xJev2YNoaiMhpN4TjzRkiPLZD'

ipfs.get(validCID, function (err, files) {
  files.forEach((file) => {
    console.log(file.path)
    console.log(file.content.toString('utf8'))
  })
})


  // request(options, (error, response, body) => {
  //   // Add any API-specific failure case here to pass that error back to Chainlink
  //   if (error || response.statusCode >= 400) {
  //
  //     callback(response.statusCode, {
  //       jobRunID: input.id,
  //       status: 'errored',
  //       error: body,
  //       statusCode: response.statusCode
  //     })
  //
  //   } else {
  //
  //     callback(response.statusCode, {
  //       jobRunID: input.id,
  //       data: body,
  //       statusCode: response.statusCode
  //     })
  //
  //   }
  // })
}

// This is a wrapper to allow the function to work with
// GCP Functions
exports.gcpservice = (req, res) => {
  createRequest(req.body, (statusCode, data) => {
    res.status(statusCode).send(data)
  })
}

// This is a wrapper to allow the function to work with
// AWS Lambda
exports.handler = (event, context, callback) => {
  createRequest(event, (statusCode, data) => {
    callback(null, data)
  })
}

// This is a wrapper to allow the function to work with
// newer AWS Lambda implementations
exports.handlerv2 = (event, context, callback) => {
  createRequest(JSON.parse(event.body), (statusCode, data) => {
    callback(null, {
      statusCode: statusCode,
      body: JSON.stringify(data),
      isBase64Encoded: false
    })
  })
}

// This allows the function to be exported for testing
// or for running in express
module.exports.createRequest = createRequest
