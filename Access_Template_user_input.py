interface = input('Enter interface type and number: ')
vlan = input('Enter vlan number: ')

access_template = ['switch mode acces',
                   'switch acc vlan {}',
                   'switchport nonegotiate',
                   'spanning-tree portfast',
                   'spannign-tree bpduguard enable']

print('\n' + '-' * 30)
print('interface {}'.format(interface))
print('\n'.join(access_template).format(vlan))