import anthropic
import os
from anthropicKey import key
from langchain_anthropic import ChatAnthropic
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

os.environ["ANTHROPIC_API_KEY"] = key

model = ChatAnthropic(model = "claude-3-5-sonnet-20241022", temperature = 0)
parser = StrOutputParser()

prompt_template = ChatPromptTemplate.from_messages(
    [
        ("system", "Translate the given code to {language} without additional explanation or text. If there is an error in the code, return only 'Error: Line' followed by the line the error is in. If a translation cannot be found, return only 'Translation not found'"),
         ("user", "{code}")
         ]
    )

chain = prompt_template | model | parser

def get_response(user, language):
    return chain.invoke(input={"code": user, "language": language})