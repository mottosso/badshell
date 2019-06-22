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

Install and experience the problem for yourself like this.

```bash
$ pip install git+https://github.com/mottosso/badshell.git --user
$ badshell cmd
> $ python
>>> import collection
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ImportError: No module named collection
```

Wops, mistyped that. Why don't I hit the Up-arrow key on your keyboard and append an `s` to that command?

Sorry, can't do that. And **that's the problem.**

<br>

### Alternatives

```bash
$ badshell powershell
# Same problem
$ badshell cmd --command python
# Same problem
```

The same problem occurs in:

- [ ] `cmd.exe`
- [ ] `powershell.exe` - Try with `badshell powershell`
- [ ] `wt.exe` - Windows Terminal Preview v0.2
- [ ] `alacritty.exe`

However history *does* work for both cmd and PowerShell in:

- [ ] `ConEmu`

But why?

<br>

### Solution

As I wrote this, I stumbled upon a related question on StackOverflow which didn't directly solve the problem, but one of the comments to an unrelated answer did.

- https://stackoverflow.com/questions/1241453/why-do-windows-consoles-lose-command-line-history-up-arrow-after-a-time#comment91693653_22481970

The problem was having a finite number of "buffers" for history, default to 4 which just so happens to be at the exact level of processes reached by this method.

![image](https://user-images.githubusercontent.com/2152766/59965565-cc83a500-9507-11e9-859d-0df5b583b41c.png)

Change these from 50/4 to 999/10 for 10 levels of 999kb each. That should do the trick.
