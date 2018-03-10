# SaltStack module example

This project contains a minimum viable SaltStack module, to show how to write one yourself.

## Requirements

SaltStack version 2017.7.4 or later.

## Running

The easiest way to run this state and test that everything works is to treat your own machine as both master and slave. In other words, run a standalone minion on your local machine.

To do this, install SaltStack and use the `salt-call` command, with a couple of options to make it completely standalone.

```
salt-call --local --file-root=${PWD} --module-dirs=${PWD}/modules --states-dir=${PWD}/states state.apply test=True
```

