#!/bin/env python
#encoding=utf-8
"""
   读、写配置文件对应section的value，封装为方法以便其他模块调用.
"""

import sys
import configparser

def get_config_elem_value(filename, section, item):
    """
        读取配置文件对应section的value.
    """
    try:
        cp = configparser.ConfigParser()
        cp.read(filename)
        value = cp.get(section, item)
        #print("read config, section : %s, item : %s, value : %s" % (section, item, value))
        return value
    except Exception as e:
        print("get_config_elem_value has exception :%s" % e)


def set_config_elem_value(filename, section, item, value):
    """
        写配置文件对应section的value.
    """
    try:
        cp = configparser.ConfigParser()
        cp.read(filename)
        cp.set(section, item, value)
        cp.write(open(filename, "w"))
        #print("write config, section : %s, item : %s, value : %s" % (section, item, value))
        return "OK"
    except Exception as e:
        print("set_config_elem_value has exception :%s" % e)
        return "ERROR"

