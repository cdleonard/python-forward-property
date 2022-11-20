import pytest

pytest.importorskip("pytest_mypy_testing")
from forward_property_test import OuterTyped


@pytest.mark.mypy_testing
def test_typed_assign():
    o = OuterTyped()
    o.x = 123  # E: Incompatible types in assignment (expression has type "int", variable has type "str")  [assignment]
    y = "abc"
    y = (
        o.y  # E: Incompatible types in assignment (expression has type "int", variable has type "str")  [assignment]
    )
