Python Forward Property
=======================

This is a simple module which implements automatic property forwarding. Like this:

```
    class Inner:
        int x = 0

    class Outer:
        Inner: inner
        x = forward_property("inner")

    def test():
        o = Outer
        o.x = 1
        assert o.inner.x == 1
```
