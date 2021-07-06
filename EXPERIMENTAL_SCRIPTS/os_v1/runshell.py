#!/usr/bin/env python3

import subprocess as sp 


def run(query):
    """execute commands with no returns, excepts status code"""
    res = sp.run(query.split())
    return res.returncode


def command(string):
    """execute commands and return resuponse"""
    return sp.check_output(string.split())