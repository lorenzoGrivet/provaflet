import flet as ft

from model.model import Model
from UI.page1_view import Page1View
from UI.page2_view import Page2View
from UI.controller import Controller


def main(page: ft.Page):
    my_model = Model() #il model per adesso è uno solo
    page1_view = Page1View(page) #pagina 1
    page2_view = Page2View(page) #pagina 2
    my_controller = Controller(page, my_model)
    my_controller.set_views(page1_view, page2_view) #setto il conroller per le due pagine
    page1_view.set_controller(my_controller)
    page2_view.set_controller(my_controller)

    # Carica entrambe le interfacce ma mostra solo la prima pagina inizialmente
    page1_view.load_interface()
    page2_view.load_interface()

    # Aggiungi i contenitori alla pagina principale
    # page.add(page1_view.container)
    # page.add(page2_view.container)

    # Mostra la prima pagina
    page1_view.container.visible = True
    page2_view.container.visible = False
    page.update()


ft.app(target=main)

"""import flet as ft



def main(page: ft.Page):
    pass


ft.app(target=main)

import flet as ft

from model.model import Model
from UI.view import View
from UI.controller import Controller


def main(page: ft.Page):
    my_model = Model()
    my_view = View(page)
    my_controller = Controller(my_view, my_model)
    my_view.set_controller(my_controller)
    my_view.load_interface()


ft.app(target=main)"""