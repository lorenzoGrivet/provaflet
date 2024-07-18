class Controller:
    def __init__(self, view, model):
        self.view=view
        self.model=model
        pass

    def goToPage1(self,e):
        self.view.tabs.selected_index=0
        self.view.update_page()
        pass

    def goToPage2(self,e):
        self.view.tabs.selected_index=1
        self.view.update_page()
        pass