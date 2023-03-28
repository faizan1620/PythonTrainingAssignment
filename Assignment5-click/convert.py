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
    try:
        click.echo(text.upper())
    except Exception as e:
        click.echo(e)

@cli.command()
@click.argument('text')
def lower(text):
    '''
        Convert to lower case
    '''
    try:
        click.echo(text.lower())
    except Exception as e:
        click.echo(e)

if __name__=="__main__":
    cli()