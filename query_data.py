import argparse
from dataclasses import dataclass
from langchain_chroma import Chroma
from langchain_community.embeddings import OpenAIEmbeddings
from langchain_openai import OpenAIEmbeddings
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic

import os

CHROMA_PATH = "chroma"
PROMPT_TEMPLATE = """
Answer the question based on the following context if it has any relevant information to answer the question. Otherwise, answer the question based on your knowledge.:

{context}

---

Answer the question based on the above context,Don't EVER say things like(the context mentions, based on the given context ..) just answer directly to the query: {question}
"""


def main():
    # Create CLI.
    parser = argparse.ArgumentParser()
    parser.add_argument("query_text", type=str, help="The query text.")
    args = parser.parse_args()
    query_text = args.query_text
    
    # Prepare the DB.
    embedding_function = OpenAIEmbeddings()
    db = Chroma(persist_directory=CHROMA_PATH, embedding_function=embedding_function)

    # Search the DB.
    results = db.similarity_search_with_relevance_scores(query_text, k=5)
    if len(results) == 0 or results[0][1] < 0.7:
        print(f"Unable to find matching results.")
        

    context_text = "\n\n---\n\n".join([doc.page_content for doc, _score in results])
    # print(f"retrieved DATA for context\n: {context_text}")
    prompt_template = ChatPromptTemplate.from_template(PROMPT_TEMPLATE)
    prompt = prompt_template.format(context=context_text, question=query_text)
    # print(prompt)

<<<<<<< HEAD
    chat = ChatOpenAI()
=======
    chat =  ChatOpenAI(temperature=0.5)
>>>>>>> 2ecb812 (fixed secret blockage from github)
    response_text = chat.invoke(prompt)
    print(f"Response: {response_text.content}")
    sources = [doc.metadata.get("source", None) for doc, _score in results]
    # formatted_response = f"Response: {response_text}\nSources: {sources}"
    print(f"sources:\n {sources}")


if __name__ == "__main__":
    main()
