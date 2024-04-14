from langchain_community.document_loaders.blob_loaders import FileSystemBlobLoader
from langchain_core.document_loaders import BaseBlobParser, Blob
from langchain_core.documents import Document
from typing import AsyncIterator, Iterator


class MyParser(BaseBlobParser):
    """A simple parser that creates a document from each line."""

    def lazy_parse(self, blob: Blob) -> Iterator[Document]:
        """Parse a blob into a document line by line."""
        line_number = 0
        with blob.as_bytes_io() as f:
            for line in f:
                line_number += 1
                yield Document(
                    page_content=line,
                    metadata={"line_number": line_number, "source": blob.source},
                )
blob_loader = FileSystemBlobLoader(path="data/books", glob="*.txt", show_progress=False)

parser = MyParser()
for blob in blob_loader.yield_blobs():
    for doc in parser.lazy_parse(blob):
        print(doc)   