"""Test-only subprocess guard. Never installed into a user's project."""

# Preload helper/probe dependencies before installing the hook so it observes
# application behavior without incidental interpreter import activity.
import argparse
import hashlib
import html
import json
import math
import os
import re
import runpy
import socket
import stat
import subprocess
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit


def deny_side_effects(event, args):
    mutations = {"os.remove", "os.rmdir", "os.rename", "os.mkdir", "os.chmod",
                 "os.truncate", "os.symlink", "os.link", "os.utime", "os.chdir",
                 "os.putenv", "os.unsetenv", "os.system", "os.startfile"}
    denied = event in mutations or event.startswith(("socket.", "subprocess.", "os.spawn", "os.exec"))
    if event == "open":
        mode, flags = args[1:3]
        denied = bool(isinstance(mode, str) and any(char in mode for char in "wax+"))
        denied |= bool(isinstance(flags, int) and flags & (os.O_WRONLY | os.O_RDWR | os.O_APPEND | os.O_CREAT | os.O_TRUNC))
    if denied:
        raise RuntimeError("read-only audit denied: " + event)


if __name__ == "__main__":
    sys.dont_write_bytecode = True
    sys.argv = sys.argv[1:]
    sys.addaudithook(deny_side_effects)
    runpy.run_path(sys.argv[0], run_name="__main__")
