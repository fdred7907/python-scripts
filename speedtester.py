import speedtest as st

server = st.Speedtest()
server.get_best_server()

#test download speed
download = server.download()
download = download/1000000
print(f"Download speed is {download}")

#test upload speed
upload = server.upload()
upload = upload/1000000
print(f"Upload Speed is {upload}")

#test ping
ping = server.results.ping
print(f"Ping Speed is {ping}")

