import pytest


class TestSampleOutput:
    @pytest.mark.parametrize(
        ('file_path', 'expected_snippet'),
        [
            ("en/_build/dirhtml/index.html", "IATI Standard 2.02 documentation"),
            ("fr/_build/dirhtml/index.html", "IATI Standard 2.02 documentation"),
        ]
    )
    def test_sample_output(self, file_path, expected_snippet):
        with open(file_path, "r") as open_file:
            file_contents = open_file.read()
            assert expected_snippet in file_contents
