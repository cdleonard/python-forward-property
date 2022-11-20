from dataclasses import dataclass, field
from types import SimpleNamespace

from typing_extensions import assert_type

from forward_property import forward_property, typed_forward_property


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


class OuterTyped:
    inner: Inner

    x = typed_forward_property[str]("inner", "x")
    y = typed_forward_property[int]("inner", "y")

    def __init__(self):
        self.inner = Inner()


def test_typed():
    o = OuterTyped()
    o.x = "aaa"
    assert_type(o.x, str)
    o2 = OuterTyped()
    assert o2.x == ""
    assert_type(o2.y, int)


@dataclass
class OuterAutoName:
    inner: Inner = field(default_factory=Inner)

    x = forward_property("inner")
    y = typed_forward_property[int]("inner")


def test_auto_name():
    o = OuterAutoName()
    o.x = "aaa"
    assert o.inner.x == "aaa"
    o.y = 123
    assert o.inner.y == 123
    o2 = OuterAutoName()
    assert o2.x == ""
