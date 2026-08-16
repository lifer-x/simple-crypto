import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class CryptoInterface(Gtk.Window):
    def __init__(self,label,action):
        self.action = action
        
        super().__init__()
        self.set_default_size(400, 300)
        self.set_position(Gtk.WindowPosition.CENTER)
        self.set_border_width(10)
        self.set_resizable(True)

        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        self.add(vbox)

        entry_frame = Gtk.Frame()
        entry_frame.set_border_width(0) 
        entry_frame.set_property("shadow-type", Gtk.ShadowType.NONE)

        entry_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=5)

        self.input_field = Gtk.Entry()
        self.input_field.set_placeholder_text("Enter text here")
        entry_box.pack_start(self.input_field, True, True, 0)

        entry_frame.add(entry_box)
        vbox.pack_start(entry_frame, True, False, 0)

        self.submit_button = Gtk.Button(label=label)
        self.submit_button.connect("clicked", self.on_submit)
        vbox.pack_start(self.submit_button, False, False, 0)

        self.connect("destroy", Gtk.main_quit)
        self.show_all()
        Gtk.main()
        
    def on_submit(self,widget):
        input_text = self.input_field.get_text() 
        result = self.action(input_text)
        self.input_field.set_text(result) 
