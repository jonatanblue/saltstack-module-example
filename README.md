# SaltStack module example

This project contains a minimum viable SaltStack module, to show how to write one yourself.

## Requirements

[SaltStack](https://docs.saltstack.com/en/latest/topics/installation/index.html) version 2017.7.4 or later.

## About the module

The `emojify` module writes your emotions as emojis to a file system of your choice.

Defining a state like this:

```
/tmp/happy:
  emojify.present:
    - emotion: happy
```

Will produce this file:
```
$ cat /tmp/happy
:D
```

## Folder structure explained

The SaltStack [execution module](https://docs.saltstack.com/en/latest/ref/modules/) and [state module](https://docs.saltstack.com/en/latest/ref/states/writing.html) reference documents provide more detailed information. This is just a brief overview.

```
.
├── modules
│   └── emojify.py
├── states
│   └── emojify.py
├── mystates.sls
└── top.sls
```

### Execution modules

The execution module `modules/emojify.py` is responsible for talking to the filesystem and making direct changes based on some instruction. It doesn't know anything about state, and just carries out some action.

### State modules

The state module `states/emojify.py` parses the state defined by the user, checks the current state of the system, compares the two and makes any changes necessary by calling the functions defined in the **execution module**.

### State files

The files ending with `.sls` contain the state as defined by the user. Written primarily in YAML (although other notation is supported), they invoke the **state module**, and tell it how the system should be configured.

The `top.sls` file is the "master" file that defines which other state files should be included. It references other files by their name, but without the `.sls` bit.

## Running

The easiest way to run and test that everything works is to treat your own machine as both master and slave. In other words, run a [standalone minion](https://docs.saltstack.com/en/latest/topics/tutorials/standalone_minion.html).

To do this, install SaltStack and use the `salt-call` command, with a couple of options to make it completely standalone.

```
salt-call --local --file-root=${PWD} --module-dirs=${PWD}/modules --states-dir=${PWD}/states state.apply
```

Command explained:

* `--local` pretends there is no Salt master and runs everything locally
* `--file-root` tells Salt in which directory to look for state (`*.sls`) files
* `--module-dirs` makes our execution module available to Salt
* `--states-dir` makes the state module available to Salt
* `state.apply` tells Salt to apply the state as defined in the `*.sls` files

