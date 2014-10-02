from rezgui.qt import QtCore, QtGui
from rezgui.mixins.ContextViewMixin import ContextViewMixin
from rezgui.widgets.StreamableTextEdit import StreamableTextEdit
from rezgui.widgets.ViewGraphButton import ViewGraphButton
from rezgui.util import create_pane
from rez.packages import Package


class VariantDetailsWidget(QtGui.QWidget, ContextViewMixin):
    def __init__(self, context_model=None, parent=None):
        super(VariantDetailsWidget, self).__init__(parent)
        ContextViewMixin.__init__(self, context_model)
        self.variant = None

        self.edit = StreamableTextEdit()
        self.edit.setStyleSheet("font: 9pt 'Courier'")
        self.view_graph_btn = ViewGraphButton(context_model)
        btn_pane = create_pane([None, self.view_graph_btn], True, compact=True)

        create_pane([self.edit, btn_pane], False, compact=True, parent_widget=self)
        self.clear()

    def clear(self):
        self.edit.clear()
        self.setEnabled(False)

    def set_variant(self, variant):
        if variant == self.variant:
            return

        if variant is None:
            self.clear()
        else:
            self.setEnabled(True)
            self.edit.clear()
            variant.print_info(self.edit, skip_attributes=("changelog",))
            self.edit.moveCursor(QtGui.QTextCursor.Start)
            self.view_graph_btn.set_variant(variant)

        self.variant = variant
