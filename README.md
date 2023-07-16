# HP-PrnStatus-DOS

## Summary
This is a simple POC for a DOS vulnerability that appears to exist in HP OfficeJet and HP LaserJet printers. This has been confirmed to affect affect multiple firmware versions including the most recent firmware version for HP OfficeJet printers.

## Method of Operation
The vulnerability is triggered by sending a valid SOAP envelope to the service hosted on the printer on TCP port 3911 that does not contain a header. Upon receiving the SOAP message, the device promptly crashes without returning a response to the sender.

## Impact
* The vulnerability appears to be a simple DOS based on the information currently known. At this time I have not found a method for escalating this to RCE or information disclosure, but I also cannot rule such a possibility out.

* HP OfficeJet printers after explotation will display a blue error screen with a hex value, then display a black error screen with the text below and will not recover without manual physical intervention.
> "Printer Error - There is a problem with the printer. Turn the printer Off, then On."

* HP LaserJet printers will blink the orange exclamation mark light, display the text below on the embedded display, then automatically restart and recover.
> "79 Service Error - Turn off then on"

* The vulnerability is pre-auth and can be exploited without any credentials on the affected device.

* The vulnerability can be exploited across networks as long as TCP 3911 is permitted between the attacker and the affected device.

* During my research, I was not able to identify a way to disable the service on 3911 or apply any local mitigations to protect the device.

## Notes
Other SOAP services appear to exist on other ports on the devices I tested, however these services did not appear to demonstrate the same vulnerability to headerless SOAP messages.
