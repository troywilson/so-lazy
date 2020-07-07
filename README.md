# So Lazy

[![Build Status](https://travis-ci.org/troywilson/so-lazy.svg?branch=master)](https://travis-ci.org/troywilson/so-lazy) [![Coverage Status](https://coveralls.io/repos/github/troywilson/so-lazy/badge.svg?branch=master)](https://coveralls.io/github/troywilson/so-lazy?branch=master) [![PyPI](https://img.shields.io/pypi/v/so-lazy)](https://pypi.org/project/so-lazy/) [![PyPI - Python Version](https://img.shields.io/pypi/pyversions/so-lazy)](https://pypi.org/project/so-lazy/) [![Apache V2 License](https://img.shields.io/badge/license-Apache%20V2-blue.svg)](https://github.com/troywilson/so-lazy/blob/master/LICENSE)

The so-lazy package allows expensive operations (i.e. API calls, complicated math) to be deferred until they are needed.


## Install

```
pip install so-lazy
```

## Usage

When the lazy decorator is called it will search the namespace scope for a loader named '_lazy_loader' (this can be overridden by the keyword loader in the lazy call ie @lazy(loader='_custom_loader')) and run it before returning to the decorated function/method.

### Function

```python
from so_lazy import lazy

_data = None

@lazy()
def get_data():
    return _data

def _lazy_loader():
    if _data is None:
        _data = load_expensive_data()

if data_needed:
    data = get_data()
```

### Class

```python
from so_lazy import lazy

class Example:

  def __init__(self):
      self._data = None

  @lazy()
  def __len__(self):
      return len(self._data)

  @lazy()
  def __getitem__(self, index):
      return self._data[index]

  def _lazy_loader():
      if self._data is None:
          self._data = load_expensive_data()

example = Example()

if data_needed:
    data = example[3]
```
