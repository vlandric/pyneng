"""
The mac list contains MAC addresses in the format XXXX:XXXX:XXXX However, in Cisco equipment MAC addresses are in XXXX.XXXX.XXXX format.

Write a code that converts MAC addresses to cisco format and adds them to a new list named result. Print the result list to the stdout using print function.

Restriction: All tasks must be done using the topics covered in this and previous chapters.
"""

mac = ["aabb:cc80:7000", "aabb:dd80:7340", "aabb:ee80:7000", "aabb:ff80:7000"]
result = []
for m in mac:
    m = m.replace(':','.')
    result.append(m)     #jednostavnije result.append(m.replace(":", "."))

print(result)

