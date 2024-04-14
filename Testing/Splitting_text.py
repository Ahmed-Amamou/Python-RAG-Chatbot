from langchain_text_splitters import RecursiveCharacterTextSplitter



# This is a long document we can split up.
with open("data/books/PFA2.txt") as f:
    pfa2 = f.read()


text_splitter = RecursiveCharacterTextSplitter(
    # Set a really small chunk size, just to show.
    chunk_size=150,
    chunk_overlap=20,
    length_function=len,
    is_separator_regex=False,
)
    
texts = text_splitter.create_documents([pfa2])
print(texts[0])
print(texts[1])
print(texts[2])