from speedtest import Speedtest

net = Speedtest()

print("Download Speed: " + str(round(net.download()/1000000,2)) + "Mbps")