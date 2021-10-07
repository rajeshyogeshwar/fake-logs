"""
This module exposes method that can be used to generate and return logs in string format. It is supposed to be used by importing the module and calling the method with necessary parameters.
"""
from datetime import datetime, timedelta

from engine.webservers.nginx import Nginx
from engine.webservers.apache import Apache


def get_nginx_webserver_log(interval: float):
    """
    A method to be used to generate logs based on supplied parameters and return them.

    :param: interval: Time interval between two consecutive logs
    :type: interval: int

    """
    dt = datetime.utcnow()
    while True:
        yield Nginx.get_log_line(dt=dt)
        dt = dt + timedelta(seconds=interval)


def get_apache_webserver_log(interval: float, format: str):
    """
    A method to be used to generate logs based on supplied parameters and return them.

    :param: interval: Time interval between two consecutive logs
    :type: interval: int

    :param: format: Apache log format [common or combined]
    :type: format: str

    """
    dt = datetime.utcnow()
    while True:
        yield Apache.get_log_line(dt=dt, format=format)
        dt = dt + timedelta(seconds=interval)
