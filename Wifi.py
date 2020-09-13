import subprocess
data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8').split('\n')

profiles = [i.split(":")[1][1:-1] for i in data if "All User Profile" in i]

print(" Copyright © 2020 Pravin singh. All Rights Reserved ")
user = "Pravin"
Pass = "@1101"

Username = input("Username: ")
Password = input("Password: ")

if user == Username and Pass == Password:
    for i in profiles:
        results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i,'key=clear']).decode('utf-8').split('\n')
        results = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]
        try:
            print ("{:<50}|  {:<}".format(i, results[0]))
        except IndexError:
            print ("{:<50}|  {:<}".format(i, ""))
elif user == Username and Pass != Password:
    print("Wrong Password")
elif user != Username and Pass != Password:
    print("Unknown User")
else :
    print("Something went Wrong")


print(" Copyright © 2020 Pravin singh. All Rights Reserved ")
