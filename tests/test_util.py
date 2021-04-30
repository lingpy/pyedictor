from pyedictor.util import *
from lingpy import Wordlist

def test_fetch():
    ds = fetch(
            "deepadungpalaung",
            to_lingpy=True,
            )
    assert ds.width == 16
    assert ds.height == 100

