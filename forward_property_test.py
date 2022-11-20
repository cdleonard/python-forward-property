from types import SimpleNamespace

from forward_property import forward_property


class Inner:
    x: str = ""
    y: int = 0


class Outer:
    inner: Inner

    x = forward_property("inner", "x")
    y = forward_property("inner", "y")

    def __init__(self):
        self.inner = Inner()


def test_inner_distinct():
    o1 = Outer()
    o1.y = 1
    o2 = Outer()
    assert o2.y == 0


def test():
    o = Outer()
    assert o.x == ""
    assert o.inner.x == ""
    assert o.y == 0
    assert o.inner.y == 0
    o.x = "hello"
    assert o.inner.x == "hello"
    o.inner.y = 3
    assert o.y == 3
    assert getattr(o.inner, "x", None) is not None
    del o.x
    assert getattr(o.inner, "x", None) == ""
    assert o.x == ""


def test_del():
    i = Inner()
    i.x = "hello"
    assert getattr(i, "x", None) == "hello"
    del i.x
    assert getattr(i, "x", None) == ""
    assert i.x == ""


def test_del_other():
    z = SimpleNamespace()
    assert getattr(z, "z", None) is None
    z.z = "zzz"
    assert getattr(z, "z", None) == "zzz"
    del z.z
    assert getattr(z, "z", None) is None


def test_setattr_return():
    i = Inner()
    a = i.x = "hello"
    assert a == "hello"
    o = Outer()
    b = o.x = "hello"
    assert b == "hello"
