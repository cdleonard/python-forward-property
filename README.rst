Python Forward Property
=======================

This is a simple module which implements automatic property forwarding.

.. code:: python

    class Inner:
        int x = 0

    class Outer:
        Inner: inner
        x = forward_property("inner")

        def __init__(self):
            self.inner = Inner()

    def test():
        o = Outer()
        o.x = 1
        assert o.inner.x == 1

Documentation is available on `github pages
<https://cdleonard.github.io/python-forward-property/docs>`__
