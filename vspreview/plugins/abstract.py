from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from ..core import ExtendedWidgetBase, Frame

if TYPE_CHECKING:
    from ..main import MainWindow


__all__ = [
    'AbstractPlugin'
]


class AbstractPlugin(ExtendedWidgetBase):
    _plugin_name: ClassVar[str]

    def __init__(self, main: MainWindow) -> None:
        try:
            super().__init__(main)
        except TypeError as e:
            print('\tMake sure you\'re inheriting a QWidget!\n')

            raise e

        self.main = main

        self.setup_ui()

        self.set_qobject_names()

    def on_current_frame_changed(self, frame: Frame) -> None:
        ...

    def on_current_output_changed(self, index: int, prev_index: int) -> None:
        ...