from converter import Converter
# Run tests from terminal with the command "pytest".
# For pytest to find tests, simply name test files test_exampleFile.py,
# and name test functions test_exampleFunction,
# and obviously have an assertion in the test function for pytest to pick up.


def test_formatLine():
    test_line = "Lorem ipsum dolor sit amet, ![[consectetur.png]] adipiscing elit, sed do [[eiusmod]] tempor incididunt ut labore et dolore magna ![[aliqua.png]]"
    test_regexp = r"\[\[.+?\]\]"
    expected_result = 'Lorem ipsum dolor sit amet, <img src = "Images/consectetur.png"></img> adipiscing elit, sed do <a src = "Notes/eiusmod"></a> tempor incididunt ut labore et dolore magna <img src = "Images/aliqua.png"></img>'
    conv = Converter("Not important", "Not important")

    print("Expected String: ", expected_result)
    print("Output String: ", conv.formatLine(test_line, test_regexp))
    assert conv.formatLine(test_line, test_regexp) == expected_result, "Output String does not match expected string."

