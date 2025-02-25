from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.chat_models import ChatOpenAI
from langchain.chains import ConversationalRetrievalChain
from langchain.memory import ConversationBufferMemory
from dotenv import load_dotenv

from config import config
import os

def create_conversation() -> ConversationalRetrievalChain:

    persist_directory = config.DB_DIR

   # Carregar as variáveis do arquivo .env
    load_dotenv()
    openai_api_key = os.getenv("OPENAI_API_KEY")

    embeddings = OpenAIEmbeddings(openai_api_key=openai_api_key)

    db = Chroma(
        persist_directory=persist_directory,
        embedding_function=embeddings
    )

    memory = ConversationBufferMemory(
        memory_key='chat_history',
        return_messages=False
    )

    qa = ConversationalRetrievalChain.from_llm(
        llm=ChatOpenAI(openai_api_key="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"),
        chain_type='stuff',
        retriever=db.as_retriever(),
        memory=memory,
        get_chat_history=lambda h: h,
        verbose=True
    )

    return qa