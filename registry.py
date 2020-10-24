import winreg

key_path = r"Software\\Microsoft\Windows\\"

reg_access = winreg.ConnectRegistry(None, winreg.HKEY_LOCAL_MACHINE)
#print(reg_access)

reg_open = winreg.OpenKey(reg_access, key_path)
#print(reg_open)

i = 0
while True:
    try:
        sub_keys = winreg.EnumKey(reg_open, i)
        print(sub_keys)
        i += 1
    except OSError:
        break