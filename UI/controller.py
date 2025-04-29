import flet as ft


class Controller:
    def __init__(self, view, model):
        self._view = view
        self._model = model

    def handle_analysis(self, e):
        self._view.txt_result.clean()
        self._view.update_page()
        if self._view.txt_dist.value.isdigit():
            grafo=self._model.airport_analysis(self._view.txt_dist.value)
            self._view.txt_result.controls.append(ft.Text(f"Numero di nodi: {grafo.number_of_nodes()}"))
            self._view.txt_result.controls.append(ft.Text(f"Numero di archi: {grafo.number_of_edges()}"))
            ## elenco_archi = grafo.edges(data='weight')
            ##for u, v, d in elenco_archi:
              ## self._view.txt_result.controls.append(ft.Text((f"{u} -- {v} : {d}")))
            self._view.update_page()
        else:
            self._view.txt_result.controls.append(ft.Text("Inserire un numero", color="red"))
            self._view.update_page()
