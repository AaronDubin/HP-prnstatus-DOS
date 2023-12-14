# HP-PrnStatus-DOS (CVE-2023-4694)

## Summary
This is a simple POC for a DOS vulnerability that has been found to affect HP OfficeJet and HP LaserJet printers. This has been confirmed to impact multiple hardware models and multiple firmware versions for these models.

## Method of Operation
The vulnerability is triggered by sending a valid SOAP envelope that does not contain a header to the service hosted on the printer on TCP port 3911. Upon receiving the SOAP message, the device crashes without returning a response to the sender.

## Impact
* The vulnerability appears to be a simple DOS based on the information currently known. At this time I have not found a method for escalating this to RCE or information disclosure, but I also cannot entirely rule such a possibility out.

* HP OfficeJet printers tested will, after exploitation, briefly display a blue error screen with a hex value followed by displaying a black error screen with the text below. The printer will not recover without manual physical intervention.
> "Printer Error - There is a problem with the printer. Turn the printer Off, then On."

* The HP LaserJet printer tested blinks the orange exclamation mark light once, blinks the green power light continuously, displays the text below on the embedded display, then automatically restarts and recovers. Because the restart process included several audible mechanical actions in the model tested, continuously looping this exploit may be able to cause premature wear or failure of the mechanical parts of the printer.
> "79 Service Error - Turn off then on"

* The vulnerability is pre-auth and can be exploited without any credentials on the affected device.

* The vulnerability can be exploited across networks as long as TCP 3911 is permitted between the attacker and the affected device.

* During my research, I was not able to identify a way to disable the service on 3911 or apply any local mitigations to protect the device.

## Mitigation
* HP has released firmware updates for multiple devices to address this issue. In testing, this POC no longer functions on firmware version 001.2337B of the HP OfficeJet 8715. Please review HP's documentation on specific models and firmwares to determine if a specific version of firmware is affected.

## Notes
Other SOAP services appear to exist on other ports on the devices I tested, however these services did not appear to demonstrate the same vulnerability to headerless SOAP messages.
This was originally discovered when a Digital Watchdog NVR system was set up on the same network segment as an affected HP printer. A packet capture revealed that the NVR was attempting to send ONVIF SOAP messages to the printer on TCP 3911 and these messages just happened to have the right characteristics to trigger the crash. If a printer started misbehaving after getting a new camera system, have another look at it - it might be just fine now!

## Confirmed Affected Models
Of the models tested, this exploit was verified to affect one or more firmware versions for the following printer models. This list is based on available models for testing and does not represent an exhaustive list.
* HP Officejet Pro 6830
* HP Officejet Pro 8715
* HP Laser Jet Pro M402dw
Note: The one FutureSmart firmware model tested did _not_ appear to have this vulnerability.

## History
* 8/1/2023 - Initiated contact with HP's PSIRT to report my findings.
* 8/8/2023 - Successfully made contact with HP's PSIRT and began knowledge transfer.
* 8/30/2023 - HP PSIRT successfully reproduced the issue on multiple, specific printer models and began developing a fix.
* 11/14/2023 - HP PSIRT was able to confirm that updated firmware was available and released for affected devices. Confirmed POC no longer functions.
* 12/14/2023 - Coordinated disclosure with HP PSIRT.

## Links
* HP Security Bulletin: https://support.hp.com/us-en/document/ish_9823639-9823677-16

## Footnote
I would like to offer my sincere appreciation and thanks to HP's PSIRT for their professionalism and thoroughness while we worked together on this. This was a new process for me and their team made it very easy for me to collaborate with them and achieve a positive result.
