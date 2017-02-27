#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
import os
import pwd
import shlex
import sys


def main():
    """Main entrypoint to the program."""
    parser = argparse.ArgumentParser(prog='setuser', description='Execute a command as a given user.')
    parser.add_argument('username', help="User to run the command as.")
    parser.add_argument('command', help="Executable to invoke.")
    parser.add_argument('args', nargs=argparse.REMAINDER, help="Arguments to command.")

    args = parser.parse_args()

    # execute it
    execute(args.username, args.command, args.args)


def execute(username, command, args):
    """Execute the given command with the given args as the user specified."""

    # validate that the given user exists
    try:
        user = pwd.getpwnam(username)
    except KeyError:
        abort("user {} not found".format(username))

    # drop to the given user
    os.initgroups(username, user.pw_gid)
    os.setgid(user.pw_gid)
    os.setuid(user.pw_uid)

    # setup the user's execution environment
    os.environ['USER'] = username
    os.environ['HOME'] = user.pw_dir
    os.environ['UID']  = str(user.pw_uid)

    try:
        os.execvp(command, [""] + args)
    except OSError as e:
        abort("cannot execute {command}: {err}".format(command=command, err=str(e)))


def abort(message, rc=1):
    sys.stderr.write("setuser: %s\n" % message)
    sys.stderr.flush()
    sys.exit(rc)


if __name__ == "__main__":
    main()
