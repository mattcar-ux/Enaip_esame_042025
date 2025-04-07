def funzione_doppio(x):
    """Questa funzione restituisce il doppio del argomento passato alla funzione"""
    return 2 * x

def funzione_quadrato(y):
    """
    Questa funzione dovrebbe prendere un numero e restituire il suo quadrato.
    Completa l'implementazione.
    """
    return y ** 2

class ClasseParzialmenteImplementata:
    def __init__(self, nome):
        self.nome = nome

    def metodo_esistente(self):
        return f"Ciao, sono {self.nome}!"

    def metodo_da_completare(self, valore:str):
        """
        Questo metodo aggiunge una stringa a self.nome
        """
        # TODO: Implementare l'aggiunta del valore e la restituzione  
        return self.nome + " " + valore