"""
Prompt the user to enter an IP address in the format 10.0.1.1. Depending on the type of address (described below), print to the stdout:

‘unicast’ - if the first byte is in the range 1-223
‘multicast’ - if the first byte is in the range 224-239
‘local broadcast’ - if the IP address is 255.255.255.255
‘unassigned’ - if the IP address is 0.0.0.0
‘unused’ - in all other cases
"""

ip = input("Enter ip address: ")

firstByte = ip.split('.')[0]

if firstByte >= "1" and int(firstByte)<223:
    print("unicast")

elif firstByte >= "224" and int(firstByte)<"239":
     print("multicast")

elif firstByte == "255" and ip == "255.255.255.255":
    print("broadcast")
elif ip == '0.0.0.0':
    print("unassigned")
else:
    print("unused")


"""
drugi nacin

ip_address = input("Enter IP address: ")
oct1 = int(ip_address.split(".")[0])

if ip_address == "255.255.255.255":
    print("local broadcast")
elif ip_address == "0.0.0.0":
    print("unassigned")
elif 1 <= oct1 <= 223:
    print("unicast")
elif 224 <= oct1 <= 239:
    print("multicast")
else:
    print("unused")
"""

