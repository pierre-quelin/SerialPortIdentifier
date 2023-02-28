# Serial Port Identifier
Program to easily list and physically identify all serial ports installed on a computer.

## Usage

* Build a dongle with a basic DB9 connector and join only pins 2 (Rx) and 3 (Tx) together.
* Disconnect all serial port connectors from the PC.
* Connect your dongle alternately to all ports
* The "control button" associated with the connected port will be switched to the selected state.
* Enjoy ;-)

## Creation of a standalone executable in order not to have to install python on the target.

### Install tox

```shell
me@mypc:~/workspace/SerialPortIdentifier$ pip install tox
```

### Build

```shell
me@mypc:~/workspace/SerialPortIdentifier$ tox
```
### Build issue

Windows vs Linux(default) see "serial.png;." vs "serial.png:." in [tox.ini](tox.ini)

Any help in resolving this command line issue with tox is welcome. TY
