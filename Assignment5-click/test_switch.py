# This script is used for demonstrating the test cases for testing any click function

from click.testing import CliRunner
from switch import sync

def test_main():
  runner = CliRunner()
  result = runner.invoke(sync)
  assert result.exit_code == 0
  assert result.output == 'Syncing\n'

if __name__=="__main__":
    test_main()