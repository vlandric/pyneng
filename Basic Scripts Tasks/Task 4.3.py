#create vlan list > ['1', '3', '10', '20', '30', '100'] < from config


config = "switchport trunk allowed vlan 1,3,10,20,30,100"
vlans = config.split()[-1].split(',')

print(vlans)




# pogresno odradjen zadatak ispod ali radi
# ["1", "3", "10", "20", "30", "100"]

vlans = ["1", "3", "10", "20", "30", "100"]

print("1 nacin")
config = 'switchport trunk allowed vlan {}'.format(",".join(vlans))
print(config)


print("2 nacin")
config = f"switchport trunk allowed vlan {','.join(vlans)}"

print(config)