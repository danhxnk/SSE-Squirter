import http.client

# User configurable variables
ServerIP = '127.0.0.1'
ServerPort = '9005'
SSEEndPoint = '/api/sse'
ReqCompleteText = ['Failed', 'Successful']

count = 0
ddata = ''
etype = ''
output = ''

#connect to SSE
conn = http.client.HTTPConnection(ServerIP + ':' + ServerPort)
conn.request('GET', SSEEndPoint)
response = conn.getresponse()

print('Welcome to the SSE Squirter')
print('___________________________')

#loop through data
while True:
    count = count + 1
    rawdata = response.fp.readline()
    string_element = rawdata.decode('UTF-8')
    if string_element[:5] == 'event':
        etype = string_element[7:] 
        etype = etype.rstrip('\r\n')
    if string_element[:4] == 'data':
        ddata = string_element[6:]
        ddata = ddata.rstrip('\r\n')
    if output != etype + ' - ' + ddata:
        output = etype + ' - ' + ddata
        print(str(count) + ' - ' + output)
    if ddata in ReqCompleteText:
        count = 0
