import pytest
from converter import Converter

def test_formatLine():
    test_line = "Lorem ipsum dolor sit amet, ![[consectetur]] adipiscing elit, sed do ![[eiusmod]] tempor incididunt ut labore et dolore magna ![[aliqua]]"
    test_regexp = r"!\[\[.+?\]\]"
    expected_result = 'Lorem ipsum dolor sit amet, <img src = "images/consectetur"></img> adipiscing elit, sed do <img src = "images/eiusmod"></img> tempor incididunt ut labore et dolore magna <img src = "images/aliqua"></img>'
    conv = Converter("Not important", "Not important")

    print("Expected String: ", expected_result)
    print("Output String: ", conv.formatLine(test_line, test_regexp))
    assert conv.formatLine(test_line, test_regexp) == expected_result, "Output String does not match expected string."

