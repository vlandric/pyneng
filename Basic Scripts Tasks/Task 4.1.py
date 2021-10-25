# replace FastEthernet with gigabith

nat = "ip nat inside source list ACL interface FastEthernet0/1 overload"

nat = nat.replace('FastEthernet0/1','GigabitEthernet0/1')

print(nat)

