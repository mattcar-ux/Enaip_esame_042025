import pytest
from progetto.prodotti_ordini import Prodotto, Ordine

def test_calcola_totale():

    prodotto_1 = Prodotto("a", 5)
    prodotto_2 = Prodotto("b", 10)

    assert prodotto_1.__str__() == "a - €5.00"

    ordine_1 = Ordine("John")

    ordine_1.aggiungi_prodotto(prodotto_1)
    ordine_1.aggiungi_prodotto(prodotto_2)

    assert ordine_1.calcola_totale() == 15