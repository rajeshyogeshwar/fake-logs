"""Constants to be used in options."""
import click

# Engine option constants
ENGINE_CHOICES = ["nginx", "apache-common", "apache-combined"]
ENGINE_HELP_MESSAGE = "Option to define tool for which to generate logs."
ENGINE_OPTION_TYPE = click.Choice(ENGINE_CHOICES, case_sensitive=False)

# Lines option constants
LINES_HELP_MESSAGE = "Number of log lines."

# Interval option constants
INTERVAL_HELP_MESSAGE = "Interval between consecutive logs."

# Mode option constants
MODE_CHOICES = ["stream", "file"]
MODE_HELP_MESSAGE = "Option to define stream or file based log generation."
MODE_OPTION_TYPE = click.Choice(MODE_CHOICES, case_sensitive=False)