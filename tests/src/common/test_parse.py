import pytest

from src.common.parse import serialize, base_lesson, lesson

FX_SERIALIZE_POSITIVE_DATA = (
    ([], [], "Expected empty list."),
    (set(), [], "Expected empty list."),
    (dict(), [], "Expected empty list."),
    (
        [base_lesson("", "", [])],
        [{"date": "", "lessons": [], "verbose": ""}],
        "Expected valid dict with empty values.",
    ),
    (
        [
            base_lesson(
                date="01.04.2020",
                verb="Середа",
                lessons=[
                    lesson(
                        number="2",
                        start="10:05",
                        stop="11:25",
                        description="some cool description about lesson",
                    )
                ],
            ),
        ],
        [
            {
                "date": "01.04.2020",
                "lessons": [
                    {
                        "number": "2",
                        "from": "10:05",
                        "to": "11:25",
                        "description": "some cool description about lesson",
                    }
                ],
                "verbose": "Середа",
            }
        ],
        "Expected dict with lessons info.",
    ),
)
FX_SERIALIZE_NEGATIVE_DATA = (
    (["", "", ""], AttributeError, "data should contain list of `base_lesson`"),
    (
        [base_lesson("", "", lesson("", "", "", ""))],
        AttributeError,
        "data should contain list of `base_lesson`",
    ),
)


class TestParse:
    @pytest.mark.parametrize(
        "data_input, expected_output, err_msg", FX_SERIALIZE_POSITIVE_DATA
    )
    def test_serialize_positive(self, data_input, expected_output, err_msg):
        actual_output = serialize(data_input)
        assert actual_output == expected_output, err_msg

    @pytest.mark.parametrize(
        "data_input, expected_exception, err_msg", FX_SERIALIZE_NEGATIVE_DATA
    )
    def test_serialize_negative(self, data_input, expected_exception, err_msg):
        with pytest.raises(expected_exception):
            serialize(data_input)
