class Events:

    def on_click(self, widget):
        print("Clic izquierdo del ratón")

    def show_text(self, widget, texto):
        self.set_text(texto)