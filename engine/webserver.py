"""Webserver log generator factory module."""

from .webservers.nginx import Nginx
from .webservers.apache import Apache


class WebserverFactory:
    """A class that provides method to generated log files for Nginx and Apache webservers."""

    def generate(engine: str, number_of_lines: int, interval: float, file_path: str):
        """Generate logs utilising the passed parameters."""
        if engine == "nginx":
            Nginx.generate_log_file(
                number_of_lines=number_of_lines, interval=interval, file_path=file_path
            )
        elif engine == "apache-common":
            Apache.generate_log_file(
                number_of_lines=number_of_lines,
                interval=interval,
                file_path=file_path,
                format="common",
            )
        elif engine == "apache-combined":
            Apache.generate_log_file(
                number_of_lines=number_of_lines,
                interval=interval,
                file_path=file_path,
                format="combined",
            )
