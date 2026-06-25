from langchain_text_splitters import RecursiveCharacterTextSplitter

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=800,
    chunk_overlap=150,
    length_function=len,
    is_separator_regex=False,
    separators=[
        "\n\n",
        "\n",
        ". ",
        "? ",
        "! ",
        "; ",
        ", ",
        " ",
        ""
    ]
)


def create_chunks(text: str):
    """Split text into overlapping chunks suitable for embeddings."""
    return text_splitter.split_text(text)