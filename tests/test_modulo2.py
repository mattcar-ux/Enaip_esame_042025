import pytest
from progetto.modulo2 import leggi_da_file, processa_dati

def test_processa_dati():
    file = [{
      "id": 1,
      "nome": "Prodotto A",
      "prezzo": 25.99,
      "attivo": True
    },
    {
      "id": 2,
      "nome": "Prodotto B",
      "prezzo": 12.50,
      "attivo": True
    }]
    assert processa_dati(file) == [1, 2]

def test_processa_dati_da_file():
    file = leggi_da_file("dati/test.json")
    assert processa_dati(file) == [1, 3, 4, 6]