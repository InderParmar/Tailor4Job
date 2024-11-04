from click.testing import CliRunner
from main import main

def test_main_help():
    runner = CliRunner()
    result = runner.invoke(main, ["--help"])
    assert result.exit_code == 0
    assert "Usage:" in result.output
    assert "--model" in result.output
    assert "--provider" in result.output
