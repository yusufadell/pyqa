"""Console script for pyqa."""
import sys

import click
from rich import print
from rich.align import Align
from rich.panel import Panel
from rich.text import Text

from pyqa import __version__
from pyqa import utils
from pyqa.constants import LOGO, URL, DEFUALT_QUERY, EPILOG


@click.group()  # invoke_without_command=True
@click.version_option(__version__, message="pyQA, version %(version)s")
@click.option("-a", "--all", is_flag=True)
@click.option(
    "-e",
    "--engine",
    help="search engine for this query (google, bing, duckduckgo)",
    default="bing",
)
@click.pass_context
def main(ctx, **kwargs):
    ctx.ensure_object(dict)
    args = ctx.obj

    query = kwargs.get("query", "yusufadell")
    args["engine"] = kwargs["engine"]
    args["all"] = kwargs["all"]


@main.command(epilog=EPILOG)
@click.argument("query", nargs=-1)
@click.pass_context
def query(ctx, **kwargs):
    args = ctx.obj

    query = kwargs["query"] or DEFUALT_QUERY
    query = " ".join(query)
    args["query"] = query

    best_link = links[0]  # TODO: iterate over links until user find his answer
    res = utils._get_answer(
        args, best_link
    )  # TODO: use pygments for syntax highlighting

    utils.display_panel(text=res)


@main.command()
@click.pass_context
def run(ctx):
    from .pyqa import pyqa

    pyqa_result = pyqa(ctx)
    # if os.name == "nt":
    #     # Windows
    #     print(pyqa_result)
    # else:
    #     utf8_result = pyqa_result.encode("utf-8", "ignore")
    #     # Write UTF-8 to stdout
    #     click.echo(utf8_result)
    click.echo(pyqa_result)


# If you have a subcommand called run taking an option called reload
# and the prefix is WEB, then the variable is WEB_RUN_RELOAD.
if __name__ == "__main__":
    main(obj={})  # pragma: no cover
