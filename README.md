# SaltStack module example

This project contains a minimum viable SaltStack module, to show how to write one yourself.

## Requirements

[SaltStack](https://docs.saltstack.com/en/latest/topics/installation/index.html) version 2017.7.4 or later.

## About the module

Writes your emotions as emojis to a file system of your choice.

Defining a state like this:

```
/tmp/happy:
  emoji.present:
    - emotion: happy
```

Will produce this file:
```
$ cat /tmp/happy
:D
```

## Running

The easiest way to run this state and test that everything works is to treat your own machine as both master and slave. In other words, run a standalone minion.

To do this, install SaltStack and use the `salt-call` command, with a couple of options to make it completely standalone.

```
salt-call --local --file-root=${PWD} --module-dirs=${PWD}/modules --states-dir=${PWD}/states state.apply
```

Command explained:

* `--local` pretends there is no Salt master and runs everything locally
* `--file-root` tells Salt in which directory to look for state (`*.sls`) files
* `--module-dirs` makes our execution module available to Salt
* `--states-dir` makes the state module available to Salt
* `state.apply` tells Salt to apply the state as defined in the `*sls` files

