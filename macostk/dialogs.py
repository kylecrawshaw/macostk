from AppKit import NSBundle, NSAlert, NSApplication, NSImage, NSPopUpButton, NSMakeRect


class BaseDialog(object):
    def __init__(self, title, message, icon=None, hide_dock=True, buttons=None):
        if hide_dock:
            self.hide_dock_icon()
        self.alert = NSAlert.alloc().init()
        self.alert.setTitle_andMessage_(title, message)
        self.alert.addButtonWithTitle_('OK')
        if icon:
            icon_image = NSImage.alloc().initWithContentsOfFile_(icon)
            self.alert.setIcon_(icon_image)

    def display(self):
        clicked_button = self.alert.runModal()
        return clicked_button


    def hide_dock_icon(self):
        bundle = NSBundle.mainBundle()
        info = bundle.localizedInfoDictionary() or bundle.infoDictionary()
        info['LSUIElement'] = '1'
        app = NSApplication.sharedApplication()


class SelectDialog(BaseDialog):
    def __init__(self, title, message, items, icon=None, hide_dock=True):
        super(SelectDialog, self).__init__(title, message, icon=icon, hide_dock=hide_dock)
        self.select_dropdown = NSPopUpButton.alloc().initWithFrame_(NSMakeRect(0, 0, 300, 24))
        self.select_dropdown.addItemsWithTitles_(items)
        self.alert.setAccessoryView_(self.select_dropdown)

    def selected(self):
        return self.select_dropdown.titleOfSelectedItem()


def ok_dialog(title, message, icon='', hide_dock=True):
    dialog = BaseDialog(title, message, icon=icon, hide_dock=hide_dock)
    return dialog.display()


def select_dialog(title, message, items, icon='', hide_dock=True):
    dialog = SelectDialog(title, message, items, icon=icon, hide_dock=hide_dock)
    dialog.display()
    return dialog.selected()
