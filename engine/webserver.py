"""Webserver log generator factory module."""

from .webservers.nginx import Nginx
from .webservers.apache import Apache

class WebserverFactory:
    """Webserver log generator factory."""

    def generate(engine: str, number_of_lines: int, interval: float, file_path: str):
        """Generate logs utilising the passed parameters."""
        if engine == "nginx":
            Nginx.generate_logs(number_of_lines=number_of_lines, interval=interval, file_path=file_path)
        elif engine == "apache-common":
            Apache.generate_logs(number_of_lines=number_of_lines, interval=interval, file_path=file_path, format="common")
        elif engine == "apache-combined":
            Apache.generate_logs(number_of_lines=number_of_lines, interval=interval, file_path=file_path, format="combined")