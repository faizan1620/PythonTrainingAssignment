import click

@click.group()
def cli():
    pass

@cli.command()
@click.argument('text')
def upper(text):
    '''
        Convert to upper case
    '''
    click.echo(text.upper())

@cli.command()
@click.argument('text')
def lower(text):
    '''
        Convert to lower case
    '''
    click.echo(text.lower())

if __name__=="__main__":
    cli()