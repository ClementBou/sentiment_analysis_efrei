import os
import sys
import pandas as pd
import pytest
import web.predict
from web.predict import predict, checking_language
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'web'))
import web.app as app


def test_url_status():
    with app.app.test_client() as client:
        resp = client.get('http://localhost:5000/')
        assert resp.status_code == 200


def test_accuracy():
    df = pd.read_csv('./tests/dataset/test.csv')
    df.dropna(inplace=True)
    df.drop_duplicates(inplace=True)
    df = df[['sentiment', 'text']]

    counter = 0
    nb_row = 300
    for row in df.sample(nb_row, random_state=1).values:
        if row[0] == web.predict.predict(row[1]).lower():
            counter += 1
    mean = counter / nb_row

    assert mean >= 0.65