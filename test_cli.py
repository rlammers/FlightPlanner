"""End-to-end tests for the flight planner command-line interface."""

import subprocess
import sys
from pathlib import Path

import pytest


PROJECT_ROOT = Path(__file__).parent
CLI_COMMAND = [sys.executable, str(PROJECT_ROOT / 'flight_planner.py')]


def run_cli(*arguments):
    """Run the CLI from the project directory and capture its result."""
    return subprocess.run(
        [*CLI_COMMAND, *arguments],
        cwd=PROJECT_ROOT,
        capture_output=True,
        check=False,
        text=True,
    )


@pytest.mark.parametrize('origin_option', ['-o', '--origin'])
def test_origin_options_create_flight_plan(origin_option):
    """Both origin option forms create the requested flight plan."""
    result = run_cli(origin_option, 'NZCH')

    assert result.returncode == 0
    assert 'Christchurch to Wellington' in result.stdout
    assert result.stdout.strip().endswith('km')
    assert result.stderr == ''


@pytest.mark.parametrize('units_option', ['-u', '--units'])
def test_units_options_select_nautical_miles(units_option):
    """Both units option forms select nautical-mile output."""
    result = run_cli('--origin', 'NZCH', units_option, 'nm')

    assert result.returncode == 0
    assert result.stdout.strip().endswith('nm')
    assert result.stderr == ''


@pytest.mark.parametrize('help_option', ['-h', '--help'])
def test_help_options_show_supported_options(help_option):
    """Both help option forms describe only supported options."""
    result = run_cli(help_option)

    assert result.returncode == 0
    assert '--origin' in result.stdout
    assert '--units' in result.stdout
    assert '-i' not in result.stdout
    assert result.stderr == ''


@pytest.mark.parametrize(
    'arguments',
    [
        (),
        ('--unknown',),
        ('--origin',),
    ],
)
def test_invalid_arguments_show_usage_without_traceback(arguments):
    """Argument errors show useful output without leaking a traceback."""
    result = run_cli(*arguments)
    output = result.stdout + result.stderr

    assert result.returncode != 0
    assert 'usage:' in output
    assert 'error:' in output
    assert 'Traceback' not in output
