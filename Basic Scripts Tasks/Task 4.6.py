# Proces the ospf_route = "       10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0" string and print the information to the stout as follows:
#Prefix                10.0.24.0/24
#AD/Metric             110/41
#Next-Hop              10.0.13.3
#Last update           3d18h
#Outbound Interface    FastEthernet0/0


ospf_route = "       10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0"

output = "\n{:25} {}"*5

route = ospf_route.replace(',',' ').replace('[','').replace(']','')
route = route.split()

print(route)

print(output.format(
    "Prefix", route[0],
    "AD/Metric", route[1],
    "Next-hop", route[2],
    "Last upadte", route[3],
    "Outbound Interface", route[4]
))