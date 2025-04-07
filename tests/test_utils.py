import pytest
from progetto.utils import scarica_dati, formatta_stringa

def test_formatta_stringa():
    assert formatta_stringa("vediamo se funziona") == "Vediamo Se Funziona"
