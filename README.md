# Transport X Chainlink Contract

### The purpose of this 'deal'

This contract is built to be used by any system or network that utilizes LINK tokens, something like a, quote on quote, protocol.
It's point is to be able to be used in combination with anything. Have it be a standalone asset.

The contract has a couple of functions:
 - Request data from the Chainlink network
 - Finding workers for a client by contacting the external adapter, and then returning the result
 - Finding workers which are close to a certain "high frequency/client traffic" location for that hour, and sends them over
 - Paying the workers for their job dependent on the data it gets from the IPFS that is implemented
 - Organizing all of the tasks
