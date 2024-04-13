from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage
from langchain_core.messages import AIMessage
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder


chat = ChatOpenAI(model="gpt-3.5-turbo-1106", temperature=0.2)

prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are a C language specialist and you should help students who are preparing for their exams with quick and concise responses. ",
        ),
        MessagesPlaceholder(variable_name="messages"),
    ]
)
chain = prompt | chat
response = chain.invoke(
    {
        "messages": [
            HumanMessage(
                content="What is the difference between a pointer and an array in C?"
            )
        ],
    }
)
print(response)

