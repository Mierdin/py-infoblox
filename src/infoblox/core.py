# Copyright (c) 2014 Marin Atanasov Nikolov <dnaeon@gmail.com>
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
# 1. Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer
#    in this position and unchanged.
# 2. Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in the
#    documentation and/or other materials provided with the distribution.
#
# THIS SOFTWARE IS PROVIDED BY THE AUTHOR(S) ``AS IS'' AND ANY EXPRESS OR
# IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES
# OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED.
# IN NO EVENT SHALL THE AUTHOR(S) BE LIABLE FOR ANY DIRECT, INDIRECT,
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT
# NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
# THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF
# THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

"""
Infoblox module for Python

The Infoblox module provides methods for getting, creating,
updating and removing objects from an Infoblox server.

"""

import requests
import ConfigParser

class InfobloxException(Exception):
    """
    Generic Infoblox Exception

    """
    pass

class Infoblox(object):
    """
    Infoblox class

    Defines methods for getting, creating, updating and
    removing objects from an Infoblox server instance.

    """
    def __init__(self, config):
        """
        Initialize a new Infoblox object instance

        Args:
            config (str): Path to the Infoblox configuration file

        """
        self.config = config

        parser = ConfigParser.ConfigParser()
        parser.read(self.config)

        try:
            self.wapi      = parser.get('Default', 'wapi')
            self.username  = parser.get('Default', 'username')
            self.password  = parser.get('Default', 'password')
            self.sslverify = parser.getboolean('Default', 'sslverify')
        except ConfigParser.NoOptionError as e:
            raise InfobloxException, 'Configuration issues detected in %s: %s' % (self.config, e)
        
        self.session        = requests.Session()
        self.session.auth   = (self.username, self.password)
        self.session.verify = self.sslverify

    def get_object(self, objtype, payload=None):
        """
        Retrieve a list of Infoblox objects of type 'objtype'

        Args:
            objtype  (str): Infoblox object type, e.g. 'network', 'range', etc.
            payload (dict): Payload with data to send

        Returns:
            A list of the Infoblox objects requested

        Raises:
            InfobloxException    

        """
        r = self.session.get(self.wapi + objtype, data=payload)

        if r.status_code != requests.codes.ok:
            raise InfobloxException, "Cannot retrieve '%s' object(s): %s [code %d]" % (
                objtype, r.content, r.status_code)

        return r.content

    def create_object(self, objtype, payload):
        """
        Create an Infoblox object of type 'objtype'

        Args:
            objtype  (str): Infoblox object type, e.g. 'network', 'range', etc.
            payload (dict): Payload with data to send

        Returns:
            The object reference of the newly create object

        Raises:
            InfobloxException

        """
        r = self.session.post(self.wapi + objtype, data=payload)

        if r.status_code != requests.codes.CREATED:
            raise InfobloxException, "Cannot create '%s' object: %s [code %d]" % (
                objtype, r.content, r.status_code)

        return r.content
    
    def update_object(self, ref, payload):
        """
        Update an Infoblox object

        Args:
            ref      (str): Infoblox object reference
            payload (dict): Payload with data to send

        Returns:
            The object reference of the updated object

        Raises:
            InfobloxException
            
        """
        r = self.session.put(self.wapi + ref, data=payload)

        if r.status_code != requests.codes.ok:
            raise InfobloxException, "Cannot update '%s' object: %s [code %d]" % (
                ref, r.content, r.status_code)

        return r.content

    def remove_object(self, ref):
        """
        Remove an Infoblox object

        Args:
            ref      (str): Object reference

        Returns:
            The object reference of the removed object

        Raises:
            InfobloxException

        """
        r = self.session.delete(self.wapi + ref)

        if r.status_code != requests.codes.ok:
            raise InfobloxException, "Cannot remove '%s' object: %s [code %d]" % (
                ref, r.content, r.status_code)

        return r.content

