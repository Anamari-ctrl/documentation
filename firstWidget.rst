========================
File upload Widget
========================

Introduction
------------
Let's start! Follow along, and at the end of the page, you will be a proud owner of the file upload widget.

.. note::
   Before you start, please make sure you have Orange installed. And some IDE to help you start developing (PyCharm, VSCode).


Widget icon
-----------

   .. image:: _static/uploadImage.png
      :alt: This icon will be used with this widget.
      :align: center

We will use this icon to represent our Widget in the Orange Canvas.




Libraries used in this widget
-----------------------------
- `NumPy <https://numpy.org/doc/>`_

   - *Usage:* Used for numerical operations and array manipulation.
   - *Why:* Provides efficient array operations and mathematical functions.

   .. code-block:: python

      import numpy as np

- **Orange Data**

    - *Usage:* Used for representing and manipulating data tables
    - *Why:* Essential for handling structured data within Orange Widgets.

    .. code-block:: python

        from Orange.data import Table

- **Orange Widgets**

   - *Usage:* Contains utilities for creating graphical user interfaces (GUIs).
   - *Why:* Provides tools for building user interfaces for Orange widgets.

   .. code-block:: python

      from Orange.widgets import gui

- **Orange Widget settings**

   - *Usage:* TODO
   - *Why:*

   .. code-block:: python

      from orangewidget.widget import settings

- **Orange Settings**

   - *Usage:* TODO
   - *Why:*

   .. code-block:: python

      from Orange.widgets.settings import Setting

- **Orange Widget**

   - *Usage:* Inherits from the `OWWidget` class, the base class for all Orange widgets.
   - *Why:* Provides the structure and functionality needed for an Orange widget.

   .. code-block:: python

      from Orange.widgets.widget import OWWidget, Input, Output, Msg

-  `AnyQt <https://anyqt.readthedocs.io/en/stable/>`_
   - *Usage:* Imports Qt widgets and components for creating the graphical user interface.
   - *Why:* Orange widgets are GUI-based, and Qt is widely used for GUIs in Python.

   .. code-block:: python

      from AnyQt.QtWidgets import QMessageBox, QGridLayout

- `PyQt5 <https://pypi.org/project/PyQt5/>`_

   - *Usage:* Imports PyQt5 widgets for file dialogs and buttons.
   - *Why:* Used for creating file dialogs and buttons in the widget's graphical user interface.

   .. code-block:: python

      from PyQt5.QtWidgets import QFileDialog, QPushButton

- `PIL <https://pillow.readthedocs.io/en/stable/>`_

   - *Usage:* Used for opening, manipulating, and saving various image file formats.
   - *Why:* Needed for image processing tasks, such as opening and saving images selected by the user.

   .. code-block:: python

      from PIL import Image

.. _metadata-section:

Metadata
--------
When defining a new Orange widget, the metadata provides information.
This section outlines key metadata attributes.

Widget Attributes
=================
This is the code you will place inside your ``uploadFile(OWWidget)`` class, that inherits from OWWidget.

.. code-block:: python

   class uploadFile(OWWidget):
        name = "Upload image"
        description = "Upload image from local directory"
        icon = "icons/uploadImage.png"
        priority = 100
        keywords = "data, load, read, open, image"
        category = "Example - documentation"

.. note::
     Priorities impact the widget's position in the toolbox.

.. tip::
     Place the widget in an appropriate category using the `category` attribute.
     In our case widgets will be placed in the documentation category.
     TODO: Lahko tudi preimenujem kategorijo


.. warning::::
   Icons specified in the `icon` attribute should be located in the correct path relative to the module where the widget is defined.

Attributes Explained
====================

- **Name Attribute**

The `name` attribute represents the display name of the widget as it appears within the Orange3 canvas. Choose a name that describes the widget's functionality.

- **Description Attribute**

The `description` attribute provides a brief and clear description of what the widget does.

- **Icon Attribute**

The `icon` attribute specifies the path to the image file used as the widget's icon. Icons contribute to the visual identification of the widget in the toolbox.

- **Priority Attribute**

The `priority` attribute determines the order in which the widget appears within its assigned category in the Orange3 toolbox.

- **Keywords Attribute**

The `keywords` attribute consists of keywords that serve as quick review of the functionality.
TODO: Sem izhajala iz tega, da recimo, izberemo res 5 kljucnih besed, ki opisejo kaj widget dela

- **Category Attribute**

The `category` attribute classifies the widget into a specific category within the toolbox.

Declaring Inputs and Outputs
----------------------------
After defining metadata, the next step is to declare Inputs and Outputs for the widget.
This widget will be the first in the workflow, so it won't receive any input.
TODO: Ker če zelis sliko prikazat/nekaj delati z njo jo je treba najprej nalozit
Therefore, we focus on declaring the Output.
In the following code snippet, we define an Output named "image," that will produce NumPy arrays as an output.
This output is set as the default, this is important if we have multiple outputs.
TODO: Ali je to pravilna razlaga? Ker ni nikjer napisano.
The widget also has control over the summary. If the `auto_summary` attribute were set to True, Orange would automatically generate a summary.
TODO: Ta auto_summary sem dodala, ker je meni metalo ven errorje, ce tega ni bilo definiranega.

.. code-block:: python

   class Outputs:
        image = Output("image", np.ndarray, default=True, auto_summary=False)

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



A concluding section summarizing the key points of the document.

.. note::

   Additional notes or important information can be included here.

.. warning::

   Highlight any warnings or important considerations here.
