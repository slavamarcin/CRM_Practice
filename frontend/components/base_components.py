from typing import Callable

from nicegui import ui


class BaseLabel(ui.label):
    def __init__(self, text: str = ''):  # get all super().__init__() args to pass them
        super().__init__(text)

        self.tag = 'label'  # specify tag for class instances


class CRMNameLabel(BaseLabel):
    def __init__(self):
        self.label_text = 'НАЗВАНИЕ crm'
        super().__init__(self.label_text)


class BaseButton(ui.button):
    def __init__(self, text: str = '', on_click: Callable = None, color: str = None, ):
        super().__init__(text, on_click=on_click, color=color)
        self.tag = 'button'
        self._text = text
        self.props(add=f'value="{text}"')


class BaseInput(ui.input):
    def __init__(self, placeholder: str = ''):
        super().__init__(placeholder=placeholder)
        self.tag = 'input'

   # @property.getter
    #def value(self):
     #   return self.value



class BaseDiv(ui.element):
    def __init__(self):
        super().__init__('div')


class BaseIcon(ui.icon):
    def __init__(self, icon_name: str):
        super().__init__(icon_name)

        self.tag = 'img'


class SideMenuOption:
    def __init__(self, icon_name: str, button_text: str):
        with BaseDiv():
            BaseIcon(icon_name)
            BaseButton(button_text)


class BaseLine(BaseDiv):
    def __init__(self):
        super().__init__()


class BaseLink(ui.link):
    def __init__(self, text: str = '', href: str = '', on_click: Callable = None):
        super().__init__(text, target=href)
        self.tag = 'a'
        self._text = text
        self.props(add=f'value="{text}"')


class BaseSelect(ui.select):
    def __init__(self, options: list, on_change: Callable = None, text: str = ''):
        super().__init__(options=options, on_change=on_change, label=text)
        # self.tag = 'select'
        # super().set_options(options)
        # self.tag = 'select'
        # self.classes(add='select')
        # self.set_options(options)


class Select(ui.element):
    def __init__(self):
        super().__init__('select')
        self.tag = 'select'
        self.classes(add='select')
        self.props(add="placeholder=\"Select a role\"")

    def set_options(self, options: list):
        with self:
            BaseLabel('Select a role !important').style('align-items: flex-start !important; color: #C0C0C0 !important;')
            for option in options:
                with ui.element('option').props(add=f'value="{option}"'):
                    BaseLabel(option)
        self._props['options'] = options
        self.update()
