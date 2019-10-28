# Transport X
## Application Concept

The idea for the entire application is that we'd have a ( kind of ) "omnipotent" agent which will organize taxi drivers and users to have them take the optimal routes.

With this, we also accomplish:
   - Less wait time for users;
   - Less polution from drivers sitting in one place or mindlessly driving around to find a client;
   - No payments needed for dispatchers for the taxi drivers;
   
## Payment system of the app

The payment is handleded by a contract in the middleware.

The steps that the contract goes through are:
  1. User finds a taxi and starts the drive ( we detect this dependent on how close the user is to the taxi that should pick him up)
  2. The drive ends ( again, automatically detected by whether the taxi driver and client are seperated by a certain distance ) , the contract calculates how much the drive should've cost using the Google Maps API Data and transfers that ammount to a "dump" wallet, it also tracks/saves a succesful drive for the taxi driver, how long it lasted, how many km, etc.
  3. At the end of the day, It takes a look at the wallet, it takes a look at the data for the taxi drivers, scales the drivers on a "how reliable/credible" scale, and then, dependent on their rank, splits the wallet's currency to the drivers
  
This payment system helps us eliminate:
   - competition between drivers;
   - fraud from taxi drivers ( ex. the drive should've cost 20$, but the driver said 25$ );
   - static prices on drives ( we are saying a STOP to different taxi meters which, dependent on the model, can make the drive cost 15$, or maybe 150$, ps, in our country this actually happens... )
   
## Future additions to the software

Some ideas we had for adding to the software which we were sadly unable to do at the moment:
 - Instant transfer from dollars ( or any other currency ) to ethereum ( and vice versa ), something like what iExec has;

## Technical Concept & Vision

Our vision for this project is for other developers to be able to freely use any part of our software as seperate packages.

For example, let's say that some developer from X country has a problem with finding taxi drivers in his city, and he wants to implement it there, but thinks that the application isn't user-friendly. Our goal is for the developer to be able to code his own front-end, use our middleware and back-end ( API ) with the middleware, cutting his work down by 2/3rd. Be able to release it and spread it as his own software.

Another example, let's say he is satisfied with the front-end, but, he thinks that maybe it's really slow or 
inaccurate, he can release his own version, re-use the same front-end and middleware, just plug-in his own API. Same examples goes for the middleware changes.

In our opinion, this should attract a lot more users to a decentralized network, without them even really knowing they're using it!
