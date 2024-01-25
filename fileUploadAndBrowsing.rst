===========
File Upload
===========

Defining file upload method
===========================

First, we add argument to the button we defined in the previous section.

.. code-block:: python

    gui.button(self.controlArea, self, label="Load image", callback=self.browse_file)


Then we define our method for browsing files, because we will use ``QFileDialog``, we
import

.. code-block:: python

    from AnyQt.QtWidgets import QFileDialog

.. code-block:: python

        def browse_file(self):
        filename, _ = QFileDialog.getOpenFileName(
            self, 'Open File', '', 'Image Files (*.gif *.jpg *.jpeg *.png *.svg);;All Files (*)'
        )
        if filename is None:
            return

        self.filename = filename
        self.load_image()

Defining load file method
==========================

Here we use NumPy, os and Output. So we add this imports:

.. code-block:: python

    import os
    import numpy as np
    from Orange.widgets.widget import Output

.. code-block:: python

        def load_image(self):
        if self.filename is None:
            self.label.setText("No file selected")
            img = None
        else:
            path = os.path.split(self.filename)
            name = path[1]
            self.label.setText(name)
            img = np.array(Image.open(self.filename))

        self.Outputs.image.send(img)

Output
===============

In the previous method we used Outputs to send our image, but we yet have to implement Outputs.
Directly under metadata we define:

.. code-block:: python

        class Outputs:
            image = Output("image", np.ndarray, default=True)


Setting
=======

We need to use Setting, which will save file, so when we close Orange, the workflow will
still remember the file, when we open Orange again. Under and outside ``class Outputs``, we
use:

.. code-block:: python

    filename = Setting(None)

Resizing
========

Till now, our window had resizing enabled. But it's better to disable this, we need to
set

.. code-block:: python

    resizing_enabled = False

Result
======

After we run ``orange-canvas``, we see our final result when we place our widget on the canvas
and click on it.

.. raw:: html

   <div style="display: flex; justify-content: space-between; text-align: center;">
      <div style="width: 48%;">
         <figcaption>Before upload</figcaption>
         <img src="_static/loadImageBox.png" alt="Image 1" style="width: 100%;">
      </div>
      <div style="width: 48%;">
         <figcaption>After upload</figcaption>
         <img src="_static/LoadImageBox2.png" alt="Image 2" style="width: 100%;">
      </div>
   </div>

|

.. warning::
   ⚠️ But if you check console from where we opened Orange, we get UserWarning.
        We need to implement summarize.


.. seealso::
   - 🔍 :doc:`summarize`