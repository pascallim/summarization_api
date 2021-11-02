from transformers import pipeline


def summarize_text(document_text: str) -> str:
  """
  Summarize document text applying Bart encoder-decoder model.

  Args:
    document_text: The text of the document.

  Returns:
    The summarized text.
  """
  summarizer = pipeline("summarization")
  summary = summarizer(document_text, max_length=130, min_length=30, do_sample=False)[0]["summary_text"]
  return summary
