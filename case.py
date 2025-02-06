"""Reger conexões e terminos de conexão na ideia de conexao
exc_typ: O tipo da exceção que ocorreu, se houver.
    se não ocorreu nenhuma exceção, este parâmetro será None.

exc_val: O tipo da exceção que ocorreu, se houver.
    se não ocorreu nenhuma exceção, este parâmetro será None.

exc_tb: O traceback (rastreamento de pilha) associado à exceção que ocorreu,
    se não ocorreu nenhuma exceção, este parâmetro será None.
"""


class AlgumaCoisa:
    def __enter__(self):
        print("Estou entrando...")

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Estou saindo.")


with AlgumaCoisa() as something:
    print("Estou no meio..")
