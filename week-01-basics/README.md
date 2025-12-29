# GOALS

## Setup Python

### Installation

Rather than using Homebrew to install python directly, I chose to install `pyenv` since it allows me to install and manage multiple python versions.

#### 1 - Install `pyenv`

```
    # install pyenv using homebrew
    ❯ brew install pyenv
```

#### 2 - Install `python3` using `pyenv`

```
    # lists available Python versions
    ❯ pyenv install --list | grep 3.11

    # install 3.11.12 since that's the latest at present
    ❯ pyenv install 3.11.12
```

#### 3. Set the `global` and `local` python3 version

```
    # check what version of python3 we are currently pointing to
    ❯ pyenv which python3
    /usr/bin/python3

    ❯ python3 --version
    Python 3.9.6

    # switch to pyenv installed version instead (both globally and locally)
    ❯ pyenv global 3.11.12

    ❯ pyenv global
    3.11.12

    # confirm python3 version we are now pointing to
    ❯ pyenv which python3
    /Users/mahesh/.pyenv/versions/3.11.12/bin/python3

    # do the same for the local version for this repo
    ❯ pyenv local 3.11.12

    ❯ pyenv local
    3.11.12

    ❯ ls -al
    total 8
    drwxr-xr-x   5 mahesh  staff  160 Dec 27 23:04 .
    drwxr-xr-x  18 mahesh  staff  576 Dec 27 21:32 ..
    drwxr-xr-x  10 mahesh  staff  320 Dec 27 21:38 .git
    -rw-r--r--   1 mahesh  staff    8 Dec 27 23:04 .python-version
    drwxr-xr-x   4 mahesh  staff  128 Dec 27 22:39 week-01-basics

    ❯ cat .python-version
    3.11.12
```

#### 4. Update your environment variables (`.zshrc`)

```
    # add these lines to .zshrc
    export PYENV_ROOT="$HOME/.pyenv"
    export PATH="$PYENV_ROOT/shims:$PATH"
    export PATH="$PYENV_ROOT/bin:$PATH"
    eval "$(pyenv init --path)"
    eval "$(pyenv init -)"

    # restart shell and confirm python version it is now pointing to
    ❯  source ~/.zshrc

    ❯ which python
    /Users/mahesh/.pyenv/shims/python

    ❯ which python3
    /Users/mahesh/.pyenv/shims/python3

    ❯ python --version
    Python 3.11.12

    ❯ python3 --version
    Python 3.11.12

```
