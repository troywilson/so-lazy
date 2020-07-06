# So Lazy

[![Build Status](https://travis-ci.org/troywilson/so-lazy.svg?branch=master)](https://travis-ci.org/troywilson/so-lazy)  ![PyPI](https://img.shields.io/pypi/v/so-lazy) ![PyPI - Python Version](https://img.shields.io/pypi/pyversions/so-lazy) [![Apache V2 License](https://img.shields.io/badge/license-Apache%20V2-blue.svg)](https://github.com/troywilson/so-lazy/blob/master/LICENSE)

Lazy loading Python package.


## Install

```
pip install so-lazy
```

## Usage

### Function

```
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

```
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
