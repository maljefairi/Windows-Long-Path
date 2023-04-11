import winreg

key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"SYSTEM\\CurrentControlSet\\Control\\FileSystem", 0, winreg.KEY_WRITE)
winreg.SetValueEx(key, "LongPathsEnabled", 0, winreg.REG_DWORD, 1)
winreg.CloseKey(key)
