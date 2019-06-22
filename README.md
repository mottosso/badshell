### Bad Shell

This repository illustrates how a **Python** instance in a subshell on **Windows** breaks history.

<br>

### Motivation

[Rez](https://github.com/mottosso/bleeding-rez) is a command-line based software provisioning and environment management system that dynamically establishes an environment that fulfills a request for versions of software and their dependencies.

It is written in Python, and thus spins up a Python instance from the command-line. This instance then spins up another shell, a "subshell" which then effectively lives as a child of the parent Python process.

So now we've got a three-level hierarchy of processes.

```bash
cmd.exe
    python.exe
        cmd.exe
```

Users then themselves in the leaf `cmd.exe`. If they were to call `python.exe` from this instance, history malfunctions.

<br>

### Usage

```bash
$ pip install git+https://github.com/mottosso/badshell.git --user
$ badshell cmd
> $ python
>>> import collection
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ImportError: No module named collection
```

Wops, mistyped that. Why don't you hit the Up-arrow key on your keyboard and append an `s` to that command? Sorry, can't do that.

**Alternatives**

```bash
$ badshell powershell
# Same problem
$ badshell cmd --command python
# Same problem
```

The same problem occurs in:

- [ ] `cmd.exe`
- [ ] `powershell.exe` - Try with `badshell powershell`
- [ ] `alacritty.exe`

However history *does* work for both cmd and PowerShell in:

- [ ] `ConEmu`

But why?
