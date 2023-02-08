---
layout: page
title: ARTToolkit
---

![logo](/assets/logo.png){:.logo}

A RedTeam Toolkit is an interactive cheat sheet, containing a useful list of offensive security tools and their respective commands/payloads, to be used in red teaming exercises.

If you hate constantly looking up the right command to use against a Windows, Linux, or Active Directory environment (like me), this project should help ease the pain a bit. Just select what information you currently have related to the victim machine (passwords, usernames, services, etc.), and it will display a list of tools you can try against the machine, along with a template command for easy copy/pasting. See the full list of [items](/items/) and [filters](/filters/).

This project was created by [Maurits Maas](https://www.linkedin.com/in/maurits-maas/) and was inspired by [GTFOBins][GTFOBins], and [LOLBAS][LOLBAS]. I relied heavily on [WADComs'][WADComs] site template to make this one.

I'm hoping to make ARTToolkit a [collaborative project][collaborative], so please feel free to [contribute][contribute] your commands.

[items]: /items/
[filters]: /filters/
[GTFOBins]: https://gtfobins.github.io/
[LOLBAS]: https://lolbas-project.github.io/
[WADComs]: https://wadcoms.github.io/
[collaborative]: https://github.com/arttoolkit/arttoolkit.github.io
[contribute]: /contribute/

{% include bin_table.html %}
