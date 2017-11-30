## py-infoblox -- Interfacing with Infoblox WAPI using Python

The `py-infoblox` module provides methods for getting, creating, updating and removing of objects from an [Infoblox](http://www.infoblox.com/) instance.

It uses the [Infoblox WAPI](https://community.infoblox.com/resource/getting-started-infoblox-web-api-wapi) in order to manage the Infoblox objects.

You might also want to check this [introduction post about py-infoblox](http://unix-heaven.org/node/106), which provides more details about `py-infoblox`.

## Requirements

* [requests](http://docs.python-requests.org/en/latest/)
* [docopt](http://docopt.org/)

## Installation

In order to install `py-infoblox` execute the command below, which will get you the `infoblox` module and the `infoblox-cli` tool installed:

	$ python setup.py install

## Configuration

Create a config file describing the various Infoblox config entries. Below is an example configuration file:

	[Default]
	wapi      = https://infoblox.example.org/wapi/v1.1/
	username  = admin
	password  = password
	sslverify = False

Now you can use the `infoblox-cli` application in order to get, create, update and remove objects from an Infoblox instance.

## Usage

Example command to get the Infoblox `network` objects:

	$ infoblox-cli -f infoblox.conf -t network get

Example command to create a new Infoblox object:

	$ infoblox-cli -f infoblox.conf -t network -d '{ "network": "192.168.2.0/24", "comment": "Test network" }' create

Example command to update an Infoblox object:

	$ infoblox-cli -f infoblox.conf -r network/ZG5zLm5ldHdvcmskMTkyLjE2OC4yLjAvMjQvMA:192.168.2.0/24/default -d '{ "comment": "The new test network" }' update

Example command to remove an Infoblox object:

	$ infoblox-cli -f infoblox.conf -r network/ZG5zLm5ldHdvcmskMTkyLjE2OC4yLjAvMjQvMA:192.168.2.0/24/default remove
