import flet as ft

class Page1View:
    def __init__(self, page: ft.Page):
        self.page = page
        self.container = ft.Column(visible=True) #uso il container per poter rendere le code visibili o no

    def set_controller(self, controller):
        self.controller = controller

    def load_interface(self):
        self.container.controls = []
        self.container.controls.append(ft.Text("Questa è la Pagina 1"))
        self.container.controls.append(ft.ElevatedButton(text="Vai alla Pagina 2", on_click=self.controller.go_to_page2))
        self.container.controls.append(ft.ElevatedButton(text="Stampa", on_click=self.controller.stampaN))
        self.lstOut= ft.ListView(expand=True)
        self.container.controls.append(self.lstOut)
        if self.container not in self.page.controls:
            self.page.add(self.container)  # Aggiunge il contenitore solo se non è già presente
        self.page.update()


