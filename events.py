from new_raid import New_raid


class Events:

    def on_click(self, widget):
       widget.connect(lambda: New_raid.show(self))

    def show_text(self, widget, texto):
        self.set_text(texto)