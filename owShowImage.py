import numpy as np
from Orange.widgets import gui
from orangewidget.widget import settings
from Orange.widgets.settings import Setting
from Orange.widgets.widget import OWWidget, Input, Output, Msg
from AnyQt.QtWidgets import QLabel, QVBoxLayout, QWidget, QInputDialog, QFileDialog
from PyQt5.QtGui import QImage, QPixmap

class ImageWidget(QWidget):
    def __init__(self, image_array):
        super().__init__()

        self.image_array = image_array
        self.init_ui()

    def init_ui(self):
        image = self.numpy_array_to_qimage(self.image_array)
        pixmap = QPixmap.fromImage(image)

        label = QLabel(self)
        label.setPixmap(pixmap)

        layout = QVBoxLayout(self)
        layout.addWidget(label)

        self.setLayout(layout)

    def numpy_array_to_qimage(self, array):
        height, width, channel = array.shape
        bytes_per_line = 3 * width
        qimage = QImage(array.data, width, height, bytes_per_line, QImage.Format_RGB888)
        return qimage

class ShowImage(OWWidget):
    name = "Image Preview"
    description = "Preview uploaded image"
    icon = "icons/showImage.jpg"
    priority = 110
    keywords = ("data", "show", "read", "open", "image")
    category = "Example - documentation"

    label = Setting("")

    class Inputs:
        image = Input("image", np.ndarray, auto_summary=False)

    class Outputs:
        image = Output("image", np.ndarray, auto_summary=False)

    proportion = settings.Setting(50)
    commitOnChange = settings.Setting(0)

    want_main_area = False
    buttons_area_orientation = False

    class Information(OWWidget.Information):
        no_file_selected = Msg("No file selected")
        no_file_saved = Msg("No file saved")

    class Warning(OWWidget.Warning):
        file_too_big = Msg("File too big")
        file_upload = Msg("Read error:\n{}")

    class Error(OWWidget.Error):
        missing_file = Msg("No file found")
        error = Msg("This is an error message")
        unknown = Msg("Read error:\n{}")

    def __init__(self):
        super().__init__()

        box = gui.widgetBox(self.controlArea, "")
        self.image_preview = ImageWidget(np.zeros((1, 1, 3), dtype=np.uint8))
        box.layout().addWidget(self.image_preview)

    @Inputs.image
    def show_image(self, image_array):
        self.image_preview = ImageWidget(image_array)
        gui.widgetBox(self.controlArea, "Image Preview").layout().addWidget(self.image_preview)

if __name__ == "__main__":
    from Orange.widgets.utils.widgetpreview import WidgetPreview

    WidgetPreview(ShowImage).run()

    main_window = ShowImage()
    main_window.show()

