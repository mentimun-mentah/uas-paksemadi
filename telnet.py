import telnetlib

HOST = "localhost"
tn = telnetlib.Telnet(HOST,"999")
tn.write(b"Hello im Telnet")
print(tn.read_all().decode('utf-8'))
