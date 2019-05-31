""" Tests for binary user terminal interaction """

import itertools
import mock
import sys
if sys.version_info.major < 3:
    import __builtin__ as stdlib
    NAME_INPUT_FUNC = "raw_input"
else:
    NAME_INPUT_FUNC = "input"
    import builtins as stdlib

import pytest
from ubiquerg import query_yes_no


def pytest_generate_tests(metafunc):
    """ Dynamic test case generation and parameterization for this module. """
    if "question" in metafunc.fixturenames:
        metafunc.parametrize("question", ["want to test?", "will this work?"])


@pytest.mark.parametrize(
    "default", [1, "a", "wontwork", [], {}, (), "Y", "N", "y", "n"])
def test_illegal_default_yields_value_error(question, default):
    """ Illegal default response causes ValueError. """
    with pytest.raises(ValueError):
        query_yes_no(question, default)


@pytest.mark.parametrize(["default", "expected"], [("no", False), ("yes", True)])
def test_query_yesno_empty_with_default(question, default, expected):
    """ Default response is used when user input is empty. """
    with mock.patch.object(stdlib, NAME_INPUT_FUNC, lambda: ""):
        assert expected is query_yes_no(question, default)


@pytest.mark.parametrize(["default", "responses", "expected"], [
    (None, ["noeffect", "N"], False),
    (None, ["meaningless", "Y"], True),
    ("no", ["illegal", "yes"], True),
    ("yes", ["invalid", "no"], False)])
def test_response_sequence(question, default, responses, expected):
    """ The interaction re-prompts and then responds as intended. """
    with mock.patch.object(stdlib, NAME_INPUT_FUNC, side_effect=responses):
        assert expected is query_yes_no(question, default)


@pytest.mark.parametrize("default", [None, "yes", "no", "YES", "NO"])
@pytest.mark.parametrize(["response", "expected"], itertools.chain(*[
    [(ans.lower(), flag), (ans.upper(), flag)] for flag, resps in
    {True: ("yes", "ye", "y"), False: ("no", "n")}.items() for ans in resps]))
def test_query_yesno_input(question, default, response, expected):
    """ Yes/No interaction responds to user input. """
    with mock.patch.object(stdlib, NAME_INPUT_FUNC, lambda: response):
        assert query_yes_no(question, default) is expected
