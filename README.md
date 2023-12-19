<p align="center"><img src="https://dydx.exchange/icon.svg?" width="256" /></p>

<h1 align="center">dYdX Chain Client for Python</h1>

<div align="center">
  <a href='https://pypi.org/project/dydx-v4-python'>
    <img src='https://img.shields.io/pypi/v/dydx-v4-python.svg' alt='PyPI'/>
  </a>
  <a href='https://github.com/amiwrpremium/dydx-v4-python/blob/master/LICENSE'>
    <img src='https://img.shields.io/pypi/l/dydx-v4-python' alt='License' />
  </a>
</div>

Python client for dYdX (v4 API).

The library is currently tested against Python versions 3.9, and 3.11.

## Installation

The `dydx-v4-python` package is available on [PyPI](https://pypi.org/project/dydx-v4-python). Install with `pip`:

```bash
pip install v4-client-py
```

## Getting Started

Sample code is located in examples folder


## Running examples

Select the file to be debugged
Select the debug button on the left
Select "Python: Current File" 

## Running tests

Integration tests uses testnet environment for testing. We use pytest.

To install pytest

```
pip install pytest
```

For read-only integration tests, run:

```
pytest -v
```

For integration tests with transactions, a subaccount must exist for the specified address.
This subaccount may be reset when testnet environment is reset. To create the subaccount, run

examples/faucet_endpoint.py

Wait for a few seconds for the faucet transaction to commit, then run

```
pytest -v -c pytest_integration.ini 
```

## License

[MIT](LICENSE)


## Disclaimer

This is not an official dYdX product. This repository is not affiliated or associated with dYdX in any way. The dYdX name, the dYdX logo, and related names, marks, emblems and images are trademarks of their respective owners.
