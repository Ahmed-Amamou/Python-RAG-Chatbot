from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from langchain_core.messages import AIMessage
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.output_parsers import StrOutputParser
from langchain.memory import ChatMessageHistory

chat = ChatOpenAI(model="gpt-3.5-turbo-1106", temperature=0.2)

prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are a C language specialist and you should help students who are preparing for their exams with quick and concise responses and you always add an example when possible. ",
        ),
        MessagesPlaceholder(variable_name="messages"),
    ]
)
output_parser = StrOutputParser()

chain = prompt | chat | output_parser
# response = chain.invoke(
#     {
#         "messages": [
#             HumanMessage(
#                 content="What is the difference between a pointer and an array in C?"
#             )
#         ],
#     }
# )

demo_ephemeral_chat_history = ChatMessageHistory()

demo_ephemeral_chat_history.add_user_message("hi!")

demo_ephemeral_chat_history.add_ai_message("Hello! How can I help you today?")



response = chain.invoke({"messages": demo_ephemeral_chat_history.messages})
print(response)

