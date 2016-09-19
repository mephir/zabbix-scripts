#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import supervisor.xmlrpc
import xmlrpclib
import argparse
from sys import exit
from pprint import pprint

def get_process_info(socket, id):
    server = xmlrpclib.ServerProxy('http://127.0.0.1',
            transport=supervisor.xmlrpc.SupervisorTransport(
                None, None,
                socket))

    return server.supervisor.getProcessInfo(id)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Get supervisor process info')
    parser.add_argument('--socket', '-s', help='Path to supervisord socket', default='unix:///run/supervisor.sock')
    parser.add_argument('id', help='ID of process')
    parser.add_argument('property', help='Status property')
    args = parser.parse_args()

    try:
        processInfo = get_process_info(args.socket, args.id)
    except xmlrpclib.Fault:
        print 'Error occured during retrieving status for %s!' % id
        exit(1)

    if args.property not in processInfo:
        print 'Property %s not found!' % args.property
        exit(1)

    print '%s' % processInfo[args.property]
    exit(0)
