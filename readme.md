# Environment

## Python version

```bash
% python3 -V
Python 3.6.5
```

## pip3

```bash
% pip3 -V
pip 10.0.1

% pip3 freeze
Flask==1.0
peewee==3.3.1
flask-cors==3.0.4
python-dateutil==2.7.2
```

# Usage

## Pre-need

## Setup

```bash
$ git clone git@github.com:kobakazu0429/radio-scheduler-server.git
$ cd radio-scheduler-server
$ pip3 install -r requirements.txt
$ python3 api.py
```

## Description

- DataBase については`datamodel.py`を参照してください

## Check

```bash
$ open http://localhost:3000/
$ open http://localhost:3000/api/v2/tasks/
$ open http://localhost:3000/api/v2/tasks/1
```

# おーまいがー

## `import.py`が動かない
