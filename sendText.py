#!/usr/bin/env python


def telegramText(message):
    import subprocess

    subprocess.call(["ntfy", "-b", "telegram", "send", message])

