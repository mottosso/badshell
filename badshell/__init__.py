"""Example of missing history from sub-subshell

On entering this subshell and calling `python`, history typically accessible
via the Up-arrow key is unavailable.

"""

import os
import argparse
import subprocess


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("shell", default="cmd")
    parser.add_argument("--command")
    opts = parser.parse_args()

    env = os.environ.copy()
    env["PROMPT"] = "> " + env.get("PROMPT", "$ ")
    args = [opts.shell]

    if opts.shell == "cmd":
        if opts.command:
            args += ["/c", opts.command]
        else:
            args += ["/k"]

    elif opts.shell == "powershell":
        if opts.command:
            args += ["-c", opts.command]
        else:
            args += ["-nologo"]

    else:
        raise ValueError(
            "'%s' not one of the supported shells ('cmd', 'powershell')"
        )

    print("Calling '%s'" % " ".join(args))
    popen = subprocess.Popen(
        args,
        env=env,
        universal_newlines=True,
    )

    exit(popen.wait())


if __name__ == '__main__':
    main()
