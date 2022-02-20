# Custom - FTP

FTP implemented using an improved version of UDP

## Usage
- Set the variables `CLIENT_IP` and `SERVER_IP` in `src/client.py` and `src/server.py`
- Specify the path to the file to be delivered in `src/server.py`. This file should be place in the `data` directory
```
data_file = open(os.path.join(HOME_DIR,'data','---filename--'), 'rb')
```
- Note that the file to be delivered must be of a 'bytestring' format, since this is the format that is written by the client script. This allows for reliable comparison of the received file with the original
- First run the client script on the receiving system, and then the server script on the sending system. The client script will terminate when the file transfer is completed, and then the server script will exit when it no longer detects a connection with the client script
```console
user@client_ip:~/custom-ftp$ python3 src/client.py
```
```console
user@server_ip:~/custom-ftp$ python3 src/server.py
```
- The variables `DATA_SIZE` and `transmission_rate` in `src/server.py`, and the socket timeout in `src/client.py` can be tuned to suit different use cases and network conditions
