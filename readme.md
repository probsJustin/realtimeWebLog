# Real Time Web Socket Log 

A really simple real time socketio log. Basically you have a python flask server set up that uses socketio and takes requests at /log and then you pass /log a parameter called body and it will post it in the websocket log. 

I will be expanding this out a bit more to include request analysis as well. 

### Endpoints: 
 - /log
	Takes a parameter of body and then logs it in the websocket log.
 - /apiTest_GET
	Takes a parameter of 'weblogUser' that sets the userID in the web log and this endpoint prints the headers of the request to the log.
	
 