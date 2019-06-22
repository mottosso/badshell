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
    parser.add_argument("--method", default="subprocess1")
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

    if opts.method == "subprocess1":
        popen = subprocess.Popen(
            args,
            env=env,
        )

        exit(popen.wait())

    elif opts.method == "execve":
        os.execve(args[0], args[1:], env)

    else:
        raise ValueError(
            "'%s' not one of the supported methods (%s)"
            % ", ".join(["subprocess1", "execve"])
        )


if __name__ == '__main__':
    main()
