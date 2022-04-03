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

Windows vs Linux see [tox.ini](tox.ini)

```shell
me@mypc:~/workspace/SerialPortIdentifier$ tox
```

### Output

```shell
me@mypc:~/workspace/SerialPortIdentifier$ tox
py39 create: /home/pierre/workspace/SerialPortIdentifier/.tox/py39
py39 installdeps: -r/home/pierre/workspace/SerialPortIdentifier/requirements.txt
py39 installed: altgraph==0.17.2,pyinstaller==4.10,pyinstaller-hooks-contrib==2022.3,pyserial==3.5
py39 run-test-pre: PYTHONHASHSEED='3991579610'
py39 run-test: commands[0] | pyinstaller --windowed --onefile --add-binary serial.png:. SerialPortIdentifier.py
36 INFO: PyInstaller: 4.10
36 INFO: Python: 3.9.2
43 INFO: Platform: Linux-5.10.0-13-amd64-x86_64-with-glibc2.31
43 INFO: wrote /home/pierre/workspace/SerialPortIdentifier/SerialPortIdentifier.spec
45 INFO: UPX is not available.
46 INFO: Extending PYTHONPATH with paths
['/home/pierre/workspace/SerialPortIdentifier']
159 INFO: checking Analysis
159 INFO: Building Analysis because Analysis-00.toc is non existent
159 INFO: Initializing module dependency graph...
160 INFO: Caching module graph hooks...
174 INFO: Analyzing base_library.zip ...
1945 INFO: Processing pre-find module path hook distutils from '/home/pierre/workspace/SerialPortIdentifier/.tox/py39/lib/python3.9/site-packages/PyInstaller/hooks/pre_find_module_path/hook-distutils.py'.
1946 INFO: distutils: retargeting to non-venv dir '/usr/lib/python3.9'
4188 INFO: Caching module dependency graph...
4300 INFO: running Analysis Analysis-00.toc
4336 INFO: Analyzing /home/pierre/workspace/SerialPortIdentifier/SerialPortIdentifier.py
4428 INFO: Processing module hooks...
4429 INFO: Loading module hook 'hook-distutils.util.py' from '/home/pierre/workspace/SerialPortIdentifier/.tox/py39/lib/python3.9/site-packages/PyInstaller/hooks'...
4430 INFO: Loading module hook 'hook-encodings.py' from '/home/pierre/workspace/SerialPortIdentifier/.tox/py39/lib/python3.9/site-packages/PyInstaller/hooks'...
4472 INFO: Loading module hook 'hook-distutils.py' from '/home/pierre/workspace/SerialPortIdentifier/.tox/py39/lib/python3.9/site-packages/PyInstaller/hooks'...
4481 INFO: Loading module hook 'hook-multiprocessing.util.py' from '/home/pierre/workspace/SerialPortIdentifier/.tox/py39/lib/python3.9/site-packages/PyInstaller/hooks'...
4482 INFO: Loading module hook 'hook-_tkinter.py' from '/home/pierre/workspace/SerialPortIdentifier/.tox/py39/lib/python3.9/site-packages/PyInstaller/hooks'...
4581 INFO: checking Tree
4581 INFO: Building Tree because Tree-00.toc is non existent
4581 INFO: Building Tree Tree-00.toc
4597 INFO: checking Tree
4597 INFO: Building Tree because Tree-01.toc is non existent
4597 INFO: Building Tree Tree-01.toc
4633 WARNING: Tcl modules directory /usr/share/tcltk/tcl8.6/../tcl8 does not exist.
4635 INFO: Loading module hook 'hook-xml.py' from '/home/pierre/workspace/SerialPortIdentifier/.tox/py39/lib/python3.9/site-packages/PyInstaller/hooks'...
4668 INFO: Loading module hook 'hook-pickle.py' from '/home/pierre/workspace/SerialPortIdentifier/.tox/py39/lib/python3.9/site-packages/PyInstaller/hooks'...
4671 INFO: Loading module hook 'hook-xml.etree.cElementTree.py' from '/home/pierre/workspace/SerialPortIdentifier/.tox/py39/lib/python3.9/site-packages/PyInstaller/hooks'...
4671 INFO: Loading module hook 'hook-heapq.py' from '/home/pierre/workspace/SerialPortIdentifier/.tox/py39/lib/python3.9/site-packages/PyInstaller/hooks'...
4673 INFO: Loading module hook 'hook-sysconfig.py' from '/home/pierre/workspace/SerialPortIdentifier/.tox/py39/lib/python3.9/site-packages/PyInstaller/hooks'...
4673 INFO: Loading module hook 'hook-difflib.py' from '/home/pierre/workspace/SerialPortIdentifier/.tox/py39/lib/python3.9/site-packages/PyInstaller/hooks'...
4675 INFO: Loading module hook 'hook-lib2to3.py' from '/home/pierre/workspace/SerialPortIdentifier/.tox/py39/lib/python3.9/site-packages/PyInstaller/hooks'...
4690 INFO: Looking for ctypes DLLs
4797 WARNING: Library Cfgmgr32 required via ctypes not found
4816 WARNING: Library Advapi32 required via ctypes not found
4834 WARNING: Library setupapi required via ctypes not found
4835 WARNING: Ignoring /System/Library/Frameworks/IOKit.framework/IOKit imported from /home/pierre/workspace/SerialPortIdentifier/.tox/py39/lib/python3.9/site-packages/serial/tools/list_ports_osx.py - only basenames are supported with ctypes imports!
4835 WARNING: Ignoring /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation imported from /home/pierre/workspace/SerialPortIdentifier/.tox/py39/lib/python3.9/site-packages/serial/tools/list_ports_osx.py - only basenames are supported with ctypes imports!
4839 INFO: Analyzing run-time hooks ...
4844 INFO: Including run-time hook '/home/pierre/workspace/SerialPortIdentifier/.tox/py39/lib/python3.9/site-packages/PyInstaller/hooks/rthooks/pyi_rth_subprocess.py'
4845 INFO: Including run-time hook '/home/pierre/workspace/SerialPortIdentifier/.tox/py39/lib/python3.9/site-packages/PyInstaller/hooks/rthooks/pyi_rth_pkgutil.py'
4847 INFO: Including run-time hook '/home/pierre/workspace/SerialPortIdentifier/.tox/py39/lib/python3.9/site-packages/PyInstaller/hooks/rthooks/pyi_rth_multiprocessing.py'
4849 INFO: Including run-time hook '/home/pierre/workspace/SerialPortIdentifier/.tox/py39/lib/python3.9/site-packages/PyInstaller/hooks/rthooks/pyi_rth_inspect.py'
4849 INFO: Including run-time hook '/home/pierre/workspace/SerialPortIdentifier/.tox/py39/lib/python3.9/site-packages/PyInstaller/hooks/rthooks/pyi_rth__tkinter.py'
4853 INFO: Looking for dynamic libraries
5356 INFO: Looking for eggs
5356 INFO: Python library not in binary dependencies. Doing additional searching...
5384 INFO: Using Python library /usr/lib/x86_64-linux-gnu/libpython3.9.so.1.0
5387 INFO: Warnings written to /home/pierre/workspace/SerialPortIdentifier/build/SerialPortIdentifier/warn-SerialPortIdentifier.txt
5412 INFO: Graph cross-reference written to /home/pierre/workspace/SerialPortIdentifier/build/SerialPortIdentifier/xref-SerialPortIdentifier.html
5423 INFO: Appending 'binaries' from .spec
5429 INFO: checking PYZ
5429 INFO: Building PYZ because PYZ-00.toc is non existent
5429 INFO: Building PYZ (ZlibArchive) /home/pierre/workspace/SerialPortIdentifier/build/SerialPortIdentifier/PYZ-00.pyz
5748 INFO: Building PYZ (ZlibArchive) /home/pierre/workspace/SerialPortIdentifier/build/SerialPortIdentifier/PYZ-00.pyz completed successfully.
5751 INFO: checking PKG
5751 INFO: Building PKG because PKG-00.toc is non existent
5751 INFO: Building PKG (CArchive) SerialPortIdentifier.pkg
9746 INFO: Building PKG (CArchive) SerialPortIdentifier.pkg completed successfully.
9753 INFO: Bootloader /home/pierre/workspace/SerialPortIdentifier/.tox/py39/lib/python3.9/site-packages/PyInstaller/bootloader/Linux-64bit-intel/run
9753 INFO: checking EXE
9753 INFO: Building EXE because EXE-00.toc is non existent
9753 INFO: Building EXE from EXE-00.toc
9753 INFO: Copying bootloader EXE to /home/pierre/workspace/SerialPortIdentifier/dist/SerialPortIdentifier
9754 INFO: Appending PKG archive to custom ELF section in EXE
9789 INFO: Building EXE from EXE-00.toc completed successfully.
___________________________________________________ summary ____________________________________________________
  py39: commands succeeded
  congratulations :)
me@mypc:~/workspace/SerialPortIdentifier$ 

```
