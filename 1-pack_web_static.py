#!/usr/bin/python3
"""Fabric script that generates a .tgz archive from the contents of the web_static folder of your AirBnB Clone repo, using the function do_pack"""
from fabric.api import local
from time import strftime
from datetime import date

def do_pack():
    """method to archive the contents of web_static folder"""
    fl_nm = strftime("%Y%m%d%H%M%S")
    try:
        local("mkdir -p versions")
        local("tar -czvf versions/web_static_{}.tgz web_static/".format(fl_nm))

        return "versions/web_static_{}.tgz".format(fl_nm)

    except Exception as e:
        return None
