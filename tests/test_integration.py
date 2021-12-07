import os
import sys
import pandas as pd
import pytest
from web.predict import predict, checking_language
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'web'))
import web.app as app


def test_url_status():
    with app.app.test_client() as client:
        resp = client.get('http://localhost:5000/')
        assert resp.status_code == 200
