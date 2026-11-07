import subprocess  # noqa: S404
import sys


def test_add_command():
    """The CLI adds two numbers."""
    result = subprocess.run(  # noqa: S603
        [sys.executable, "-m", "hpc_tutorial", "1", "1"],
        check=True,
        capture_output=True,
        text=True,
    )
    assert result.stdout.strip() == "2"
