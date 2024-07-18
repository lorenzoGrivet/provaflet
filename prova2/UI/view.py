import flet as ft

class View(ft.UserControl):

    def __init__(self,page=ft.Page):
        super().__init__()
        self.btn2 = None
        self.btn1 = None
        self.lst1 = None
        self.lst2 = None
        self.page=page
        self.controller=None
        self.tabs= None
        self.tab1=None
        self.tab2=None

    def loadInterface(self):
        self.tabs=ft.Tabs()

        self.tab1=ft.Tab(text="Tab 1",content=self.createContent1())
        self.tab2=ft.Tab(text="Tab 2",content=self.createContent2())


        self.tabs.tabs.append(self.tab1)
        self.tabs.tabs.append(self.tab2)

        self.page.add(self.tabs)
        self.page.update()

        pass

    def createContent1(self):

        self.lst1=ft.ListView()
        self.btn1= ft.ElevatedButton(text="Tab2",on_click=self.controller.goToPage2,width=100)
        self.lst1.controls.append(ft.Text("listview 1"))
        self.txt1=ft.TextField(label="aaaa")
        self.txt2=ft.TextField(label="aaaa")
        self.dd1=ft.Dropdown(options=[ft.dropdown.Option("a")])
        content = ft.Column(controls=[ft.Container(self.lst1,width=100),ft.Container(self.btn1,width=100),ft.Container(self.dd1),ft.Container(ft.Row(controls=[self.txt1,self.txt2]))],horizontal_alignment=ft.CrossAxisAlignment.CENTER,width=600)

        return content

    def createContent2(self):

        self.lst2=ft.ListView()
        self.btn2= ft.ElevatedButton(text="Tab1",on_click=self.controller.goToPage1)
        self.dd2=ft.Dropdown(options=[ft.dropdown.Option("a")])
        content = ft.Row(controls=[ft.Container(self.lst2,width=100),ft.Container(self.btn2,width=100),ft.Container(self.dd2)],vertical_alignment=ft.CrossAxisAlignment.START)
        return content

    def set_controller(self, controller):
        self.controller = controller

    def update_page(self):
        self.page.update()
        pass
