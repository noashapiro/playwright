import os

import pytest

CHROMIUM_PATH = "/opt/pw-browsers/chromium_headless_shell-1194/chrome-linux/headless_shell"


@pytest.fixture(scope="session")
def browser_type_launch_args():
    args = {"args": ["--no-sandbox", "--disable-dev-shm-usage"]}
    if os.path.exists(CHROMIUM_PATH):
        args["executable_path"] = CHROMIUM_PATH
    return args
