========================
File upload Widget
========================

Introduction
------------
Welcome to the documentation for the "Image Upload" widget, the first in a series dedicated to image processing with Orange.
This widget serves as a simple yet essential tool for uploading image datasets,
laying the foundation for subsequent widgets designed to enhance and analyze image data in your Orange workflows.

Widget icon
-----------

We will use this icon with the first icon.

   .. image:: _static/uploadImage.png
      :alt: This icon will be used with this widget.



Libraries used in this widget
-----------------------------
#. **NumPy**

   - *Usage:* Used for numerical operations and array manipulation.
   - *Why:* Provides efficient array operations and mathematical functions.

   .. code-block:: python

      import numpy as np

#. **Orange Data**

    - *Usage:* Used for representing and manipulating data tables
    - *Why:* Essential for handling structured data within Orange Widgets

    .. code-block:: python

        from Orange.data import Table

#. **Orange Widgets**

   - *Usage:* Contains utilities for creating graphical user interfaces (GUIs).
   - *Why:* Provides tools for building user interfaces for Orange widgets.

   .. code-block:: python

      from Orange.widgets import gui

#. **Orange Widget settings**

   - *Usage:* Likely contains classes and functions for handling widget settings.
   - *Why:* Used for managing and handling widget settings.

   .. code-block:: python

      from orangewidget.widget import settings

#. **Orange Settings**

   - *Usage:* Defines a specific setting class.
   - *Why:* Used to define and manage specific settings for the `UploadFile` widget.

   .. code-block:: python

      from Orange.widgets.settings import Setting

#. **Orange Widget**

   - *Usage:* Inherits from the `OWWidget` class, the base class for all Orange widgets.
   - *Why:* Provides the structure and functionality needed for an Orange widget.

   .. code-block:: python

      from Orange.widgets.widget import OWWidget, Input, Output, Msg

#. **AnyQt**

   - *Usage:* Imports Qt widgets and components for creating the graphical user interface.
   - *Why:* Orange widgets are GUI-based, and Qt is widely used for GUIs in Python.

   .. code-block:: python

      from AnyQt.QtWidgets import QMessageBox, QGridLayout

#. **PyQt5**

   - *Usage:* Imports PyQt5 widgets for file dialogs and buttons.
   - *Why:* Used for creating file dialogs and buttons in the widget's graphical user interface.

   .. code-block:: python

      from PyQt5.QtWidgets import QFileDialog, QPushButton

#. **PIL**

   - *Usage:* Used for opening, manipulating, and saving various image file formats.
   - *Why:* Needed for image processing tasks, such as opening and saving images selected by the user.

   .. code-block:: python

      from PIL import Image

Meta data - defining a widget
-----------------------------

Input and Output code snippet
-----------------------------

Include code snippets using the following format::

   .. code-block:: python

      # Your Python code here

Conclusion
-----------

A concluding section summarizing the key points of the document.

.. note::

   Additional notes or important information can be included here.

.. warning::

   Highlight any warnings or important considerations here.
