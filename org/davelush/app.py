import argparse
import logging

from org.davelush.setup_logging import initialise_logging


def parse_cli_args(command_line, environment):
    """
    Parses command line arguments
    :param command_line:
    :param environment:
    :return:
    """
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--log-level",
        default=environment.get("LOG_LEVEL", logging.DEBUG),
        type=int,
        help="Default logging level for the application",
    )

    arguments = parser.parse_args(command_line)
    return arguments



def main(command_line, environment):
    # gimme some configuration & logging
    config = parse_cli_args(command_line, environment)
    if not config:
        return 1
    initialise_logging(config.log_level)

    logging.info("Hello World")
