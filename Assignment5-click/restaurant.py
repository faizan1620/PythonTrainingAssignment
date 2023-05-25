import click


@click.group()
def cli():
    pass


@cli.group()
def lunch():
    pass


@cli.group()
def dinner():
    pass


@lunch.command()
def burger():
    print("Enjoy your burger")


@dinner.command()
def pizza():
    print("Enjoy your pizza")


if __name__ == "__main__":
    cli()
