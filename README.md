
# Transport X

## Concept

Proof of concept of a decentralized and self-organizing/ownerless company, capable of regulating and advancing itself, with complete user data privacy and integrity, which also serves the workers.

## Technical

#### It consists of 3 main parts:
  1. The Ethereum smart contract has all the functions necessary for the company to operate, it keeps track of accounts, data and tasks all on its own.
  2. The Chainlink middleware is used to connect the smart contract with the API & artificial intelligence.
  3. The Artificial Intelligence & back-end is run on the iExec distributed computing network.

### How it works

  To prove the concept we've created a taxi company. Drivers can subscribe and work for the company, clients can request rides from it, and the company organizes the drivers, finds workers for the clients and learns to be more efficient in its work.

### Finding a worker

  1. A client requests a ride from the smart contract and provides all the necessary data.
  2. The smart contract makes a call to the API using Chainlink, and provides the API with all the necessary data.
  3. The API analyzes it and finds the best worker for the task based on drivers location.
  4. The selected driver is returned to the smart contract and he is assigned a task.
  5. The driver executes the task.
  6. The client pays the company and rates the driver.

### Organizing workers

  The company efficiency is connected to the amount of resources the workers waste, such as time and fuel.

  1. The contract calls the AI in the API.
  2. The AI predicts how many clients might request a cabbie, and where they might request it from, filters that data and then returns the updates to the contract.
  3. The contract based on the AI's prediction gives tasks to drivers.
  4. The drivers then execute their task.

## Data flow

  TBA

## Economic model

  The company pays its workers based on the time and the resources they have spent. Some of the criteria are as follows:
   - How much time the worker has spent with the company
   - Their rating
   - How many rides they've taken

## Benefits

Clients, workers and the people of Earth gain many benefits from using the software.

### Clients
Some of the benefits that cleints gain are:
 - Evading fraud since the payment system calculates how much the drive should cost and auto-magically gets paid.
 - Static prices, in the sense, it doesn't really matter if you took a cab in one city or another. The price for that country will be the same ( per km ) based on it's economy and laws.
 - Less wait time for a taxi to get to their location.

### Workers
Workers benefits:
 - No more volatility to whether they'll manage to find clients.
 - With the previous benefit, they also gain cooperation, or in other words, competition between them(who gets the passenger).
 - The company doesn't take extra cuts for things like dispatchers for example, so all of their work will be 'fully' paid.
 - Less work needed like setting up where the drive started or ended. All of it is automatic.
 
 ### The world
 Due to the previously mentioned benefits, all of us gain the next benefits as well:
  - Less polution from cabbies just mindlessly waiting.

### Something extra
Since this is meant to be used as a protocol, in the sense of it being modular ( every piece of this software being it's own seperate entity ), developers can use anything here to make their own application using parts of our software. With this we hope we will attract more people to use decentralized networks, sometimes without even knowing that they're using them!


## Advancing

  1. The Ethereum smart contract makes a call to the API using Chainlink, and sends all its acquired data.
  2. The AI learns on the data collected.
  3. Updating the algorithm in the API to use the rating as a criteria for matching a worker with a client.
  4. Instant transfer from dollars ( or any other currency ) to ethereum ( and vice versa ), something like what iExec has.
  4. Working with fondations and companies which would like to donate to users and taxi drivers which use our application because they are aware about the impact of car pollution and work with us to try and minimize it.


## Easier navigation

#### The API & AI: https://github.com/PegasusMKD/transport_x/tree/api/PegasusMKD/transport_x

#### The Front-End: https://github.com/PegasusMKD/transport_x/tree/front-end

#### The Contract: https://github.com/PegasusMKD/transport_x/tree/chainlink_contract

#### The Chainlink External Adapter: https://github.com/PegasusMKD/transport_x/tree/chainlink_external_adapter

#### The Script/Code which calls IExec: TBA ( To be added )

## Team

#### David I.          https://github.com/id997
#### Filip J.          https://github.com/PegasusMKD
#### Nikola S.    

## Catching up with the Coders

#### Web URL: https://eprotocols.org/

Updates,patches and changes will be posted on that URL. There is also an e-mail address where you can contact us <3
