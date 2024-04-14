from langchain_community.document_loaders import PyPDFLoader
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings

loader = PyPDFLoader("data/books/Tunisia.pdf")
pages = loader.load_and_split()

print(type(pages[0]))
# print("metadata:") 
# print(pages[1].metadata)


# faiss_index = FAISS.from_documents(pages, OpenAIEmbeddings())
# docs = faiss_index.similarity_search("demographic", k=2)
# for doc in docs:
#     with open("output.txt", "w") as f:
#         f.write(str(doc.metadata["page"]) + ": " + doc.page_content[:300])