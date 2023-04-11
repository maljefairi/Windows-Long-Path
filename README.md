# PLEASE open CMD in windows as ADMINISTRATOR first

# Windows-Long-Path
if you are trying to install long files links and windows does not allow you and you get this error as example 
Installing collected packages: tensorflow-intel, tensorflow
ERROR: Could not install packages due to an OSError: [Errno 2] No such file or directory: 'C:\\Users\\nethe\\AppData\\Local\\Packages\\PythonSoftwareFoundation.Python.3.11_qbz5n2kfra8p0\\LocalCache\\local-packages\\Python311\\site-packages\\tensorflow\\include\\external\\com_github_grpc_grpc\\src\\core\\ext\\filters\\client_channel\\lb_policy\\grpclb\\client_load_reporting_filter.h'
HINT: This error might have occurred since this system does not have Windows Long Path support enabled. You can find information on how to enable this at https://pip.pypa.io/warnings/enable-long-paths
# the python script fixes this issue.
i created this script to automate this process and make it run 
Here is a Python script that can enable Windows Long Path support by modifying the Windows Registry
Here is a Python script that can enable Windows Long Path support by modifying the Windows Registry:

import winreg

key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"SYSTEM\\CurrentControlSet\\Control\\FileSystem", 0, winreg.KEY_WRITE)
winreg.SetValueEx(key, "LongPathsEnabled", 0, winreg.REG_DWORD, 1)
winreg.CloseKey(key)
This script opens the FileSystem key in the Windows Registry and sets the value of LongPathsEnabled to 1, which enables Long Path support. After running this script, you will need to restart your computer for the changes to take effect.

Please note that modifying the Windows Registry can be risky and can cause system instability if not done correctly. Make sure you understand the risks and consequences before running this script.
# alternative manual way to fix this issue doing the following:
It appears that you're encountering an issue due to the Windows long path limitation. To resolve this issue, you can enable long path support on your system. Here's a step-by-step guide on how to enable long path support on Windows:

Type "regedit" in the Windows search bar and press Enter to open the Registry Editor.

Navigate to the following key in the Registry Editor:

arduino
Copy code
HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\FileSystem
Look for an entry named LongPathsEnabled on the right side of the Registry Editor window. If it doesn't exist, you can create it by right-clicking on the "FileSystem" key, selecting "New" > "DWORD (32-bit) Value", and then naming the new entry "LongPathsEnabled".

Double-click on the LongPathsEnabled entry to open its properties.

Change the "Value data" field to 1 and click "OK".

Close the Registry Editor and restart your computer.


