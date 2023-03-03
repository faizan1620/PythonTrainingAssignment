import click

class AliasedGroup(click.Group):
    def get_command(self, ctx, cmd_name):
        rv = click.Group.get_command(self, ctx, cmd_name)
        if rv is not None:
            return rv
        matches = [x for x in self.list_commands(ctx)
                   if x.startswith(cmd_name)]
        if not matches:
            return None
        elif len(matches) == 1:
            return click.Group.get_command(self, ctx, matches[0])
        ctx.fail(f"Too many matches: {', '.join(sorted(matches))}")

    def resolve_command(self, ctx, args):
        # always return the full command name
        _, cmd, args = super().resolve_command(ctx, args)
        return cmd.name, cmd, args

@click.group(cls=AliasedGroup)
def cli():
    '''
    Example to demonstrate alias name also work like pul for pull command etc
    '''
    pass

@cli.command()
def push():
    click.echo("Pushing to the repo")

@cli.command()
def pull():
    click.echo("Pulling from the repo")

if __name__=="__main__":
    cli()