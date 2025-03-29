from new_raid import NewRaid


class Events:

    def on_click(self, widget):
       widget.connect(lambda: NewRaid.show(self))

    def show_text(self, widget, texto):
        self.set_text(texto)