"""Log generator module."""
import click

from constants import (
    ENGINE_OPTION_TYPE,
    ENGINE_HELP_MESSAGE,
    LINES_HELP_MESSAGE,
    INTERVAL_HELP_MESSAGE,
)
from engine.webserver import WebserverFactory


@click.command()
@click.option(
    "--engine", "-e", required=True, type=ENGINE_OPTION_TYPE, help=ENGINE_HELP_MESSAGE
)
@click.option("--lines", "-l", required=True, type=int, help=LINES_HELP_MESSAGE)
@click.option("--interval", "-i", type=float, default=1, help=INTERVAL_HELP_MESSAGE)
@click.option(
    "--file_path",
    "-f",
    required=True,
    type=str,
    help="Absolute file path to write logs to.",
)
def generate_fake_logs(engine, lines, interval, file_path):
    """
    fake-logs is a command line to generate fake logs that can be used for testing. Currently it supports generating logs for Nginx in the default combined format and for Apache webserver in common log format and combined log format as well.
    """
    if engine in ["nginx", "apache-common", "apache-combined"]:
        WebserverFactory.generate(
            engine=engine, number_of_lines=lines, interval=interval, file_path=file_path
        )
    else:
        print("I am working on adding new engines to generate logs.")
