import http.client, urllib.parse
key = 'GGENZQXAFQUSZFWU' # copy the API key

t=int(22)

while True:
    t=t+1
    print ("temperature",t)
    params=urllib.parse.urlencode({'field1':t,'key':key})
        # This line prepares data to be sent as part of the HTTP request
    headers={"Content-type":"application/x-www-form-urlencoded","Accept":"text/plain"}
        #This line defines HTTP headers for the POST request
    con=http.client.HTTPConnection("api.thingspeak.com")
        # This establishes an HTTP connection to api.thingspeak.com, the server where the data will be sent
        # con becomes an object that represents this connection, allowing us to send and receive data
    con.request("POST","/update",params,headers)
        # This line sends an HTTP POST request
    response=con.getresponse()
        # This line retrieves the server’s response after sending the POST request.
        # response is an object containing details about the HTTP response
    print (response.status,response.reason)
        # This line prints the HTTP response’s status code and reason phrase
    con.close()
        # This line closes the HTTP connection to free up resources and complete the transaction.