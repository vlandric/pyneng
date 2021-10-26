
""""
Task 4.8
Convert the IP address in the ip variable to binary and print output in columns to stdout:

the first line must be decimal values
the second line is binary values
The output should be ordered in the same way as in the example output below:

in columns
column width 10 characters (in binary you need to add two spaces between columns to separate octets among themselves)
Example output for address 10.1.1.1:

10        1         1         1
00001010  00000001  00000001  00000001
"""

ip = "192.168.3.1"
ip_list = ip.split('.')

print(f"{ip_list[0]:8} {ip_list[1]:8} {ip_list[2]:8} {ip_list[3]:8}")
print(f"{int(ip_list[0]):08b} {int(ip_list[1]):08b} {int(ip_list[2]):08b} {int(ip_list[3]):08b}")

#drugi nacin
octets = ip.split(".")

output = """
{0:<10}{1:<10}{2:<10}{3:<10}
{0:08b}  {1:08b}  {2:08b}  {3:08b}"""

print(output.format(int(octets[0]), int(octets[1]), int(octets[2]), int(octets[3])))