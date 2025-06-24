import os

print('''
--------------------------
Linux Menu Based Project
----------------------------
    1.Date command
    2.cal command
    3.ifconfig
    4.ls
    5.pwd
    6.whoami
    7.uname -a
    8.df -h
    9.free -m
    10.uptime
    11.who
'''
     )


choice = int(input("Enter your Choice:"))

if choice == 1:
    user = input("Enter Username:")
    ip = input("Enter your remote ip:")
    os.system(f"ssh {user}@{ip} date")
elif choice == 2:
    user = input("Enter Username:")
    ip = input("Enter your remote ip:")
    os.system(f"ssh {user}@{ip} cal")
elif choice == 3:
    user = input("Enter Username:")
    ip = input("Enter your remote ip:")
    os.system(f"ssh {user}@{ip} ifconfig")
elif choice == 4:
    user = input("Enter Username:")
    ip = input("Enter your remote ip:")
    os.system(f"ssh {user}@{ip} ls")
elif choice == 5:
    user = input("Enter Username:")
    ip = input("Enter your remote ip:")
    os.system(f"ssh {user}@{ip} pwd")
elif choice == 6:
    user = input("Enter Username:")
    ip = input("Enter your remote ip:")
    os.system(f"ssh {user}@{ip} whoami")
elif choice == 7:
    user = input("Enter Username:")
    ip = input("Enter your remote ip:")
    os.system(f"ssh {user}@{ip} uname -a")
elif choice == 8:
    user = input("Enter Username:")
    ip = input("Enter your remote ip:")
    os.system(f"ssh {user}@{ip} df -h")
elif choice == 9:
    user = input("Enter Username:")
    ip = input("Enter your remote ip:")
    os.system(f"ssh {user}@{ip} free -m")
elif choice == 10:
    user = input("Enter Username:")
    ip = input("Enter your remote ip:")
    os.system(f"ssh {user}@{ip} uptime")
elif choice == 11:
    user = input("Enter Username:")
    ip = input("Enter your remote ip:")
    os.system(f"ssh {user}@{ip} who")
