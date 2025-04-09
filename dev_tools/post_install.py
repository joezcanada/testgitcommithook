# post_install.py
import subprocess
import sys


def install_autohooks():
    subprocess.check_call([sys.executable, "-m", "pip", "install", "autohooks"])
    subprocess.check_call(
        [ sys.executable, "-m", "pip", "install", "autohooks-plugin-black", "autohooks-plugin-ruff", ]
    )
    subprocess.check_call(
        [sys.executable, "-m", "autohooks", "activate", "--mode", "pythonpath"]
    )


if __name__ == "__main__":
    install_autohooks()
