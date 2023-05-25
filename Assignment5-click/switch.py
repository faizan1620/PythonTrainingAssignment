import click


@click.group()
@click.option(
    "--switch/--no-switch", default=False, help="Using as a toggle if switch is on/off"
)
def cli(switch):
    click.echo(f"Switch is {'on' if switch else 'off'}")


@cli.command()
def sync():
    click.echo("Syncing")


if __name__ == "__main__":
    sync()
