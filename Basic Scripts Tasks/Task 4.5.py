# create list from common vlans


command1 = "switchport trunk allowed vlan 1,2,3,5,8"
command2 = "switchport trunk allowed vlan 1,3,8,9"

vlans1 = command1.split()[-1].split(",")
print(vlans1)
vlans2 = command2.split()[-1].split(",")
print(vlans2)
vlans = set(vlans2).intersection(set(vlans1))


print(list(vlans))

#a little bit better  solution
command1 = "switchport trunk allowed vlan 1,2,3,5,8"
command2 = "switchport trunk allowed vlan 1,3,8,9"

vlans1 = command1.split()[-1].split(",")
vlans2 = command2.split()[-1].split(",")

result = sorted(set(vlans1) & set(vlans2))
print(result)