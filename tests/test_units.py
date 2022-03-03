import pandas as pd
import pytest

import web.predict
from time import time

def test_checking_language():
    assert web.predict.checking_language("I hate all of them") == 1
    with pytest.raises(Exception):
        web.predict.predict.checking_language("Je les déteste tous")

def test_toxicity_degree():
    assert max(web.predict.predict(str("I want to kill you"))) == "toxicity"

def test_toxic_sentence():
    assert web.predict.predict(str("I hate you"))["toxicity"] >= 0.3

def test_not_toxic_sentence():
    assert web.predict.predict(str("I love you"))["toxicity"] < 0.3

def test_stress():

    counter = 0
    nb_requested_row = 100

    end = time() + 60
    while time() < end:
        web.predict.predict(str("I hate all of them"))
        counter += 1

    assert counter >= nb_requested_row
    print(end)

