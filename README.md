# iwlib - interface with wireless tools in Linux

iwlib is a package for interfacing with iwlib, providing an implementation to
the wireless tools in Linux.

While very incomplete at the moment, it aims to eventually become a complete
implementation, as features become necessary. If you find some functionality
missing, feel free to contribute to the project, or create an issue on the bug
tracker.

Currently it provides what I consider the bare minimum to become useful -
scanning, setting the ESSID of a device, and getting the current configuration
back from a device.

http://www.hpl.hp.com/personal/Jean_Tourrilhes/Linux/Tools.html

## Installation
------------

Installation requires the Python developer tools, and wireless_tools package
for compilation. If Python.h and iwlib.h exist on your system, you should be
good to go.

`$ pip install iwlib`

Depending on your linux distro, the package name may change. But this is tested on Ubuntu 17
`$ sudo apt-get install libiw-dev`


## Change History
--------------

1.5 (1st October 2014)
    - Added support for Python 3

1.4 (12th June 2014)
    - Fixed incompatibility with wireless_tools version 30.pre9
    - Fixed build error that resulted in iwconfig and iwlist not being built.
    - Minor cleanups
    - Feels "snappier"

1.3.1 (2nd April 2013)
    - Fixed packaging issue involving missing header files.

1.3 (24th March 2013)
    - Added ``iwlib.utils module``. See documentation for details.
    - Added ``iwlib.iwlist module``. See documentation for details.
    - Added function ``set_essid``, to ``iwlib.iwconfig``.

1.2.1 (21st March 2013)
    - Initial release of code, as it was when I inherited it.
    
## Quick Guide
--------------
Run following command in a shell to see the available wireless interfaces  
`$ iwconfig `

('wlan0' is very common, so that is what we will use for this quick guide)  

In the python Shell,   
`>> import iwlib`  
`>> interface = 'wlan0'`  
`>> iwlib.get_iwconfig(interface)`  
` {'BitRate': b'72.2 Mb/s', 'ESSID': b'AP_SSID', 'Access Point': b'AP_MAC', 'stats': {'quality': 45, 'noise': 0, 'updated': 75, 'level': 191}, 'Frequency': b'2.422 GHz', 'Mode': b'Managed'}`
 
The dict's values are byte strings. You can use `b'xyz'.decode('utf-8')` to decode them into python strings.

Finally, here's the docstring for the function  
`>> print(iwlib.get_iwconfig.__doc__)`  
` Retrieve the current configuration of an interface. `  
` Arguments:`  
`  - device to work on (e.g. eth1, wlan0). `
`
