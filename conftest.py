import pytest


@pytest.fixture(scope="session")
def browser_type_launch_args():
    """Point playwright at the pre-installed Chromium binary."""
    return {
        "executable_path": "/opt/pw-browsers/chromium_headless_shell-1194/chrome-linux/headless_shell",
        "args": ["--no-sandbox", "--disable-dev-shm-usage"],
    }
