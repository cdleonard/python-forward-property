"""
Module implementing property forwarding for python objects
"""

__version__ = "0.1.0"

from typing import Generic, Optional, TypeVar


class forward_property:
    """A descriptor for property forwarding"""

    __slots__ = ("inner", "prop")

    inner: str
    prop: str

    def __init__(self, attr: str, prop: Optional[str] = None):
        self.inner = attr
        if prop is not None:
            self.prop = prop

    def __set_name__(self, outer, name) -> None:
        if not hasattr(self, "prop"):
            self.prop = name

    def __get__(self, outer, owner=None):
        return getattr(getattr(outer, self.inner), self.prop)

    def __set__(self, outer, value) -> None:
        setattr(getattr(outer, self.inner), self.prop, value)

    def __delete__(self, outer) -> None:
        delattr(getattr(outer, self.inner), self.prop)


GetSetType = TypeVar("GetSetType")


class typed_forward_property(Generic[GetSetType]):
    """A descriptor for property forwarding with an annotated get/set type"""

    __slots__ = ("inner", "prop")

    inner: str
    prop: str

    def __init__(self, attr: str, prop: Optional[str] = None):
        self.inner = attr
        if prop is not None:
            self.prop = prop

    def __set_name__(self, outer, name) -> None:
        if not hasattr(self, "prop"):
            self.prop = name

    def __get__(self, outer, owner=None) -> GetSetType:
        return getattr(getattr(outer, self.inner), self.prop)

    def __set__(self, outer, value: GetSetType) -> None:
        setattr(getattr(outer, self.inner), self.prop, value)

    def __delete__(self, outer) -> None:
        delattr(getattr(outer, self.inner), self.prop)
