import flet as ft

class Controller:
    def __init__(self, page, model):
        self.page = page
        self.model = model

    def set_views(self, page1_view, page2_view):
        self.page1_view = page1_view
        self.page2_view = page2_view

    def go_to_page1(self, e): #alterno la visibilità delle pagine
        self.page1_view.container.visible = True
        self.page2_view.container.visible = False
        self.page.update()

    def go_to_page2(self, e):
        self.page1_view.container.visible = False
        self.page2_view.container.visible = True
        self.page.update()


    def stampaN(self,e):
        numeri=self.model.numeri
        for n in numeri:
            self.page1_view.lstOut.controls.append(ft.Text(n))
        self.page1_view.page.update()


    def stampaL(self,e):
        lettere=self.model.lettere
        for n in lettere:
            self.page2_view.lstOut.controls.append(ft.Text(n))
        self.page2_view.page.update()
        pass
