import subprocess, re, os

print("""Welcome to DNS changer
DNS servers list:
     ________________________________________
     | DNS server name  | DNS server number |
     |--------------------------------------|
     |    Cloudflare    |       (1)         |
     |--------------------------------------|
     |      Google      |       (2)         |
     |--------------------------------------|
     |     OpenDNS      |       (3)         |
     |--------------------------------------|
     |      Shecan      |       (4)         |
     |--------------------------------------|
     |     Azad(403)    |       (5)         |
     |--------------------------------------|
     |>>>>>>>> created by D4rk $ide <<<<<<<<|
     ----------------------------------------
     """)
x = input("select dns: ")
a = input("""select your os:
	___________________________
	| OS name |   OS number   |
	|-------------------------|
	|  Linux  |      (1)      |
	|-------------------------|
	| Windows |      (2)      |
	|-------------------------|
	|   Mac   | Coming soon...|
	|-------------------------|
""")
if a == "1":
    if x == "1":
        os.system("echo nameserver 1.1.1.1 > /etc/resolv.conf && echo nameserver 1.0.0.1 >> /etc/resolv.conf")
        print("Done!")
    elif x == "2":
        os.system("echo nameserver 8.8.8.8 > /etc/resolv.conf && echo nameserver 8.8.4.4 >> /etc/resolv.conf")
        print("Done!")
    elif x == "3":
        os.system("echo nameserver 208.67.222.222 > /etc/resolv.conf && echo nameserver 208.67.220.220 >> /etc/resolv.conf")
        print("Done!")
    elif x == "4":
        os.system("echo nameserver 178.22.122.100 > /etc/resolv.conf && echo nameserver 185.51.200.2 >> /etc/resolv.conf")
        print("Done!")
    elif x == "5":
        os.system("echo nameserver 10.202.10.202 > /etc/resolv.conf && echo nameserver 10.202.10.102 >> /etc/resolv.conf")
        print("Done!")
    else:
        print("please type your dns server number.")
elif a == "2":
    cmd_net_check = subprocess.run(['ipconfig', '/all'], capture_output=True).stdout.decode()
    net_find = str(re.findall("Ethernet adapter (.*):", cmd_net_check))
    if x == 1:
        cmd_dns_set = subprocess.run(
            ['netsh', 'interface', 'ip', 'set', 'dns', f'name="{net_find.strip("['']")}"', 'static', '1.1.1.1'])
        cmd_dns_set1 = subprocess.run(
            ['netsh', 'interface', 'ip', 'add', 'dns', f'name="{net_find.strip("['']")}"', '1.0.0.1', 'index=2'])
    elif x == 2:
        cmd_dns_set = subprocess.run(
            ['netsh', 'interface', 'ip', 'set', 'dns', f'name="{net_find.strip("['']")}"', 'static', '8.8.8.8'])
        cmd_dns_set1 = subprocess.run(
            ['netsh', 'interface', 'ip', 'add', 'dns', f'name="{net_find.strip("['']")}"', '8.8.4.4', 'index=2'])
    elif x == 3:
        cmd_dns_set = subprocess.run(
            ['netsh', 'interface', 'ip', 'set', 'dns', f'name="{net_find.strip("['']")}"', 'static', '208.67.222.222'])
        cmd_dns_set1 = subprocess.run(
            ['netsh', 'interface', 'ip', 'add', 'dns', f'name="{net_find.strip("['']")}"', '208.67.220.220', 'index=2'])
    elif x == 4:
        cmd_dns_set = subprocess.run(
            ['netsh', 'interface', 'ip', 'set', 'dns', f'name="{net_find.strip("['']")}"', 'static', '178.22.122.100'])
        cmd_dns_set1 = subprocess.run(
            ['netsh', 'interface', 'ip', 'add', 'dns', f'name="{net_find.strip("['']")}"', '185.51.200.2', 'index=2'])
    elif x == 5:
        cmd_dns_set = subprocess.run(
            ['netsh', 'interface', 'ip', 'set', 'dns', f'name="{net_find.strip("['']")}"', 'static', '10.202.10.202'])
        cmd_dns_set1 = subprocess.run(
            ['netsh', 'interface', 'ip', 'add', 'dns', f'name="{net_find.strip("['']")}"', '10.202.10.102', 'index=2'])
    else:
        print("please type your dns server number.")