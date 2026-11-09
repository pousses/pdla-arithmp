"""Arithmp: Command-line interface for the Arithmp package."""

from pathlib import Path

import click

from arithmp.parser import Parser, ParserException


@click.command()
@click.option(
    "-c",
    "command",
    type=str,
    required=False,
    default=None,
    help="run the expression given in the command line",
)
@click.argument("args", nargs=-1, type=click.UNPROCESSED)
def main(command: str | None, args: tuple[str, ...]) -> None:
    """
    Main entry point for the Arithmp command-line interface.
    """
    parser = Parser()
    if command is not None:
        try:
            if (result := parser.parse(None, command)) is not None:
                click.echo(result)
        except ParserException as e:
            click.echo(
                f"Error in command at line {e.context.line} column {e.context.column} '{e.context.source}': {e}"
            )

    else:
        filepath = Path(args[0])
        try:
            if (result := parser.parse(filepath, filepath.read_text())) is not None:
                click.echo(result)
        except ParserException as e:
            click.echo(
                f"Error in script '{filepath}' at line {e.context.line} column {e.context.column} '{e.context.source}': {e}'"
            )


if __name__ == "__main__":
    main()
