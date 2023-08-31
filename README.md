# HP-PrnStatus-DOS

## Summary
This is a simple POC for a DOS vulnerability that appears to exist in HP OfficeJet and HP LaserJet printers. This has been confirmed to affect affect multiple firmware versions including the most recent firmware version for HP OfficeJet printers.

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

## Notes
Other SOAP services appear to exist on other ports on the devices I tested, however these services did not appear to demonstrate the same vulnerability to headerless SOAP messages.

## Confirmed Affected Models
Of the models tested, this exploit was verified to affect one or more firmware versions for the following printer models. This list is based on available models for testing and does not represent an exhaustive list.
* HP Officejet Pro 6830
* HP Officejet Pro 8715
* HP Laser Jet Pro M402dw
The one FutureSmart firmware model tested did _not_ appear to have this vulnerability.
