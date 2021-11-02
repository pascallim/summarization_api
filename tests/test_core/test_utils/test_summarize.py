import unittest
from unittest.mock import patch, MagicMock
from core.utils import summarize


class TestSummarize(unittest.TestCase):

    @patch("core.utils.summarize.pipeline")
    def test_summarize_text(self, mock_pipeline):
        # Given
        text = "input_text"
        expected_summary = "output_text"
        mock_summarizer = MagicMock()
        mock_pipeline.return_value = mock_summarizer
        mock_summarizer.return_value = [{"summary_text": expected_summary}]
        # When
        summary = summarize.summarize_text(text)
        # Then
        self.assertEqual(summary, expected_summary)
