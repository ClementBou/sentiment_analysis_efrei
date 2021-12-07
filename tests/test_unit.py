import pandas as pd
import pytest
import web.predict


def test_positive_sentiment():
    assert web.predict.predict("I am happy today") == "Positive"


def test_neutral_sentiment():
    assert web.predict.predict("There is a cat in the street") == "Neutral"


def test_negative_sentiment():
    assert web.predict.predict("Paul is not satisfied of his work") == "Negative"


def test_checking_language():
    assert web.predict.checking_language("Paul is not satisfied of his work") == 1
    with pytest.raises(Exception):
        web.predict.predict.checking_language("Je suis ici")


def test_accuracy():
    df = pd.read_csv('./tests/dataset/test.csv', encoding='unicode_escape')
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