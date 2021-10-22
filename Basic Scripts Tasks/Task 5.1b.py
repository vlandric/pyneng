"""
 Modify the script from task 5.1a so that, when requesting a parameter, a list of possible parameters was displayed. The list of parameters must be obtained from the dictionary, rather than written manually.

Display information about the corresponding parameter of the specified device.

An example of script execution:

$ python task_5_1b.py
Enter device name: r1
Enter parameter name (ios, model, vendor, location, ip): ip
10.255.0.1
Restriction: You cannot modify the london_co dictionary.

All tasks must be completed using only the topics covered. That is, this task can be solved without using the if condition.
"""



london_co = {
    "r1": {
        "location": "21 New Globe Walk",
        "vendor": "Cisco",
        "model": "4451",
        "ios": "15.4",
        "ip": "10.255.0.1"
    },
    "r2": {
        "location": "21 New Globe Walk",
        "vendor": "Cisco",
        "model": "4451",
        "ios": "15.4",
        "ip": "10.255.0.2"
    },
    "sw1": {
        "location": "21 New Globe Walk",
        "vendor": "Cisco",
        "model": "3850",
        "ios": "3.6.XE",
        "ip": "10.255.0.101",
        "vlans": "10,20,30",
        "routing": True
    }
}

device = input("enter device name: ")

params = ",".join(london_co[device].keys())

parameter = input(f"Enter parameter name ({params})  ")

print(london_co[device][parameter])

