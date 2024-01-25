=========
Summarize
=========

.. warning::
   ⚠️  UserWarning: register 'summarize' function for type ndarray.

To correct this warning, we need to implement summarize. First, we import:

.. code-block:: python

    from orangewidget.utils.signals import summarize, PartialSummary

Then we implement:

.. code-block:: python

    @summarize.register
    def summarize_ndarray(a: np.ndarray):
        return PartialSummary(f"{a.shape[0]}x{a.shape[1]}", f"Image of size {a.shape[0]}x{a.shape[1]}")

When we run ``orange-canvas`` we see the partial summary under the info box, and
if we click on it, we get whole summary:

.. image:: _static/summary.png
    :alt: Image size summary.
    :Align: center
