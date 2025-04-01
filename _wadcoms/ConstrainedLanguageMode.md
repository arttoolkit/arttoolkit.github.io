---
description: |
  Determining the PowerShell Constrained Language Mode is important for assessing security restrictions on script execution. Constrained Language Mode limits certain operations, such as COM object creation and .NET calls, which can impact payload execution.

command: |
  $ExecutionContext.SessionState.LanguageMode

items:
  - Shell
services:
  - General
  - AV
OS:
  - Windows
attack_types:
  - Enumeration
references:
  - https://www.ired.team/offensive-security/code-execution/powershell-constrained-language-mode-bypass
---