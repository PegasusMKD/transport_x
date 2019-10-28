# Transport X API
## About it's implementation

The API is pretty much entirely decentralized. It is deployed on iExec which is a decentralized computing hub. It uses Docker with a Ubuntu image as it's base. It's already uploaded as an app on iExec, currently in the process of registering for the dApp Marketplace.

Python version: 3.6.6

Dependencies it relies on:
 - keras
 - sklearn
 - pandas
 - NumPy
 - shapely
 - geopy

## About it's features

The 3 features that it currently supports are:
  - An algorithm which finds the closest taxi driver to the user/client that is requesting it, and adds it to a dataset
  - AI which predicts where the next batch of users will be on an hourly basis
  - It's also a 'self-training' AI, it has an open socket/port ( function ) which can be called with a request at any time of the day ( or night ;-) so that it retrains itself on the new dataset
  
Currently, our accuracy isn't really all that great(stable 22% without overfitting), but, we are certain that it will go up once we get real-world data, compared to trying to simulate where users would 'spawn' on the map, and then training it on that. We will also get some other data we might need to make it more precise like the weather for example.

