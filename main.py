from speedtest import Speedtest
print("Test working now...")
net = Speedtest()
print("Download Speed: " + str(round(net.download()/1000000,2)) + "Mbps")
print("Upload Speed: " + str(round(net.upload()/1000000,2)) + "Mbps")
print("Finish!")