
# Transport X

## Concept

Proof of concept of a decentralized and ownerless company, capable of regulating and advancing itself, with complete user data privacy and integrity,
that serves the workers.

## Technical

    It consist of 3 main parts.
  1. The Ethereum smart contract has all the functions necessary for the company to operate, it takes care keeping track of accounts, data and tasks.
  2. The Chainlink middleware is used to connect the smart contract with the artificial intelligence.
  3. The Artificial Intelligence is run on the Iexec distributed computing network.

## How it works

  To prove the concept we have created  a taxi company. Drivers can subscribe and work for the company, clients can request rides from the company, and the company organizes the drivers, finds drivers for the clients and learns to be more efficient in its work.

#Finding a worker

  1. A client requests a ride from the smart contract and provides all the necessary data.
  2. The smart contract makes a call to the AI using Chainlink, and provides the AI with all the necessary data.
  3. The AI does an analysis and finds the best worker for the task based on drivers location, credibility and rating.
  4. The selected driver is returned to the smart contract and he is assigned a task.
  5. The driver executes the task.
  6. The client pays the company and rates the driver.


#Advancing

  1. The Ethereum smart contract makes a call to the AI using Chainlink, and sends all its acquired data.
  2. The AI learns on this data.


#Organizing workers

  The company efficiency is connected to the amount of resources the workers waste, such as time and fuel.

  1. The contract calls the AI.
  2. The AI chooses the amount of drivers that will be online and chooses the location of the drivers, And returns the updates to the contract.
  3. The contract based on the AI answer gives tasks to the drivers.
  4. The drivers execute their task.

#Economic model

  The company pays its workers based on the time and the resources they have spent.

#Data flow

  TBA


## Easier navigation

#### The AI: https://github.com/PegasusMKD/transport_x/tree/api/PegasusMKD/transport_x

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
