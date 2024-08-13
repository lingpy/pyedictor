# PyEDICTOR: Simple Access to EDICTOR Databases

**+++ PyEDICTOR is deprecated and superseded by the [`edictor`](https://github.com/digling/edictor) package.+++**




## Installation:

```
$ pip install edictor[lingpy]
```

## Usage

```python
>>> from edictor.wordlist import fetch_wordlist as fetch
>>> wl = fetch("deepadungpalaung", to_lingpy=True)
>>> print(wl.width)
16
```

To load as a LexStat wordlist:

```python
>>> from lingpy import *
>>> from edictor.wordlist import fetch_wordlist as fetch
>>> lex = fetch("deepadungpalaung", to_lingpy=True, transform=LexStat)
```

To convert your dataset to EDICTOR format from CLDF:

```
$ edictor wordlist -d cldf/cldf-metadata.json mydataset
```

This will create a wordlist file `mydataset.tsv` from your CLDF data located in `cldf/cldf-metadata.json`.


