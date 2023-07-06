# commpay-healthcheck

This script is used to conduct healthcheck on database connections on a list of CommPay sites. Both the obtaining of the list of CommPay sites and healthcheck for each site are to be done through REST API calls.

## How to use the script

It is recommended to use **Python 3.9.x** and later, as well as a Python virtual environment in which to execute the script, so as not to mess with the Python main environment in your machine. Once the virtual environment has been activated, install the required modules using the command `python -m pip install -r requirements.txt` (while the current working directory is in the root directory of this repo).

Make sure you are connected to one of the Iress VPN gateways before executing the script; this is so the REST API calls would push through. Execute the script in the command line through `main.py`.
