#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import supervisor.xmlrpc
import xmlrpclib

p = xmlrpclib.ServerProxy('http://127.0.0.1',
        transport=supervisor.xmlrpc.SupervisorTransport(
            None, None,
            'unix:///run/supervisor.sock'))

print p.supervisor.getState()
