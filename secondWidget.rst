=====================
Image Preview Widget
=====================


Introduction
------------
Since we already have a widget that uploads an image, why don't we create a widget, that will show the image we just
uploaded.


Widget icon
-----------

   .. image:: _static/showImage.jpg
      :alt: This icon will be used with this widget.
      :align: center

We will use this icon to represent our Widget in the Orange Canvas.




Libraries used in this widget
-----------------------------

   .. code-block:: python

        import numpy as np
        from Orange.widgets import gui
        from orangewidget.widget import settings
        from Orange.widgets.settings import Setting
        from Orange.widgets.widget import OWWidget, Input, Output, Msg
        from AnyQt.QtWidgets import QLabel, QVBoxLayout, QWidget, QInputDialog, QFileDialog
        from PyQt5.QtGui import QImage, QPixmap

If you are wondering why we used libraries listed above, please check out the explanation here: :doc:`firstWidget` .


.. _metadata-section:

Metadata
--------
When defining a new Orange widget, the metadata provides information. This section outlines key metadata attributes.


Widget Attributes
=================
This is the code you will place inside your ``ShowImage(OWWidget)`` class, that inherits from OWWidget.

.. code-block:: python

   class ShowImage(OWWidget):
        name = "Image Preview"
        description = "Preview uploaded image"
        icon = "icons/showImage.jpg"
        priority = 110
        keywords = ("data", "show", "read", "open", "image")
        category = "Example - documentation"

.. note::

   📌  We have priority set to 110 because we want to place this widget in the second position in our category.


.. warning::

   ⚠️ Icons specified in the `icon` attribute should be located in the correct path relative to the module where the widget is defined.



Registration with Orange
------------------------

We run the ``orange-canvas`` command, after we should see this in the toolbox.
Since we specified the category, our widgets will be placed in that category - so far we have two widgets. The second
widget in the category should be shown now.

   .. image:: _static/category.png
      :alt: This is our category.
      :align: center

This widget looks a little different from the first widget. We see dots on both sides - which means we can connect

   .. image:: _static/imagePreviewOnCanvas.png
      :alt: This icon will be used with this widget.
      :align: center

Declaring Inputs and Outputs
----------------------------

.. code-block:: python

    class Inputs:
        image = Input("image", np.ndarray, auto_summary=False)

    class Outputs:
        image = Output("image", np.ndarray, auto_summary=False)

.. _widget-settings:

Widget Settings
---------------

Tukaj bi potrebovala razlago, zakaj te elemente definiramo, ker ni nikjer razlozeno, samo uporabi se.

.. code-block:: python

    proportion = settings.Setting(50)
    commitOnChange = settings.Setting(0)
    want_main_area = False
    buttons_area_orientation = False


Classes for Information, Warning and Error
------------------------------------------
Base widget has already implemented different classes that help us warn users.
You can use them like this:

.. code-block:: python

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




Widget Initialization
---------------------

.. code-block:: python

     def __init__(self):
        super().__init__()
        self.image_preview = ImageWidget(np.zeros((1, 1, 3), dtype=np.uint8))

Here we create an instance of the ImageWidget class and initializing
it with a small black image
(1x1 pixels with three color channels) filled with zeros.
This serves as an placeholder image for the image_preview widget.

.. code-block:: python

     box = gui.widgetBox(self.controlArea, "")
     box.layout().addWidget(self.image_preview)

ImageWidget class declaration
-----------------------------
ImageWidget class is designed to display images in a Qt-based GUI.
The class takes a NumPy array as input, converts it to a QImage,
and displays it within a vertical box layout.

.. warning::
   ⚠️ Place this class above Show Image class


.. code-block:: python

    class ImageWidget(QWidget):
        def __init__(self, image_array):
            super().__init__()

            self.label = QLabel(self)
            self.init_ui()

            # Set the initial image
            self.update_image(image_array)

        def init_ui(self):
            layout = QVBoxLayout(self)
            layout.addWidget(self.label)
            self.setLayout(layout)

        def update_image(self, new_image_array):
            image = self.numpy_array_to_qimage(new_image_array)
            pixmap = QPixmap.fromImage(image)
            self.label.setPixmap(pixmap)

        def numpy_array_to_qimage(self, array):
            height, width, channel = array.shape
            bytes_per_line = 3 * width
            qimage = QImage(array.data, width, height, bytes_per_line, QImage.Format_RGB888)
            return qimage



Handle loaded image file
------------------------

.. code-block:: python

    @Inputs.image
    def show_image(self, image_array):
        self.image_preview.update_image(image_array)

The last part of the code is adding image preview to our layout. Now we can run and test the code!

.. note::
    📌 Decorator ``@Inputs.image``: handles incoming image data from the specified input signal

.. warning::
    ⚠️ Before running, make sure you add this to the bottom of the code.
        .. code-block:: python

            if __name__ == "__main__":
                from Orange.widgets.utils.widgetpreview import WidgetPreview

                WidgetPreview(ShowImage).run()

                main_window = ShowImage()
                main_window.show()


Our first workflow
------------------
Here we create our first workflow. First we use the file load widget and connect it to
image preview where we can see the image.

.. image:: _static/workflow1.png
    :alt: Workflow example.
    :align: center


Now the best part, we can finally check how our image preview looks!

.. image:: _static/imagePreview.png
    :alt: Image preview window.
    :align: center


Conclusion
----------

We are now ending the first half of the tutorial. I must warn you, the next two widgets are a
bit more complex, but actually I had a lot more fun when I was creating them.

.. seealso::
   - :doc:`thirdWidget`
