"""Log generator module."""
import click

from constants import *
from engine.webserver import WebserverFactory


@click.command()
@click.option("--engine", "-e", required=True, type=ENGINE_OPTION_TYPE, help=ENGINE_HELP_MESSAGE)
@click.option("--lines", "-l", required=True, type=int, help=LINES_HELP_MESSAGE)
@click.option("--interval", "-i", type=float, default=1, help=INTERVAL_HELP_MESSAGE)
@click.option("--file_path", "-f", required=True, type=str, help="Absolute file path to write logs to.")
def fake_log_generator(engine, lines, interval, file_path):
    """Log generator."""
    WebserverFactory.generate(engine=engine, number_of_lines=lines, interval=interval, file_path=file_path)
