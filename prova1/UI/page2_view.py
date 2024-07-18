import flet as ft

class Page2View:
    def __init__(self, page: ft.Page):
        self.page = page
        self.container = ft.Column(visible=False)

    def set_controller(self, controller):
        self.controller = controller

    def load_interface(self):
        self.container.controls = []
        self.container.controls.append(ft.Text("Questa è la Pagina 2"))
        self.container.controls.append(ft.ElevatedButton(text="Vai alla Pagina 1", on_click=self.controller.go_to_page1))
        self.page.update()
        self.container.controls.append(ft.ElevatedButton(text="Stampa", on_click=self.controller.stampaL))
        self.lstOut = ft.ListView(expand=True)
        self.container.controls.append(self.lstOut)
        if self.container not in self.page.controls:
            self.page.add(self.container)  # Aggiunge il contenitore solo se non è già presente
        self.page.update()


