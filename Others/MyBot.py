import os as os
import pandas as pd
import logging as lg
import langchain as lc
from langchain_groq import ChatGroq
from langchain.prompts import ChatPromptTemplate
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.document_loaders import WebBaseLoader 

def get_user_agent() -> str:
    """Get user agent from environment variable."""
    env_user_agent = os.environ.get("USER_AGENT")
    if not env_user_agent:
        v_log.warning(
            "USER_AGENT environment variable not set, "
            "consider setting it to identify your requests."
        )
        return "DefaultLangchainUserAgent"
    return env_user_agent

v_apik = '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'
os.environ['GROQ_API_KEY'] = v_apik
v_model_chat = ChatGroq(model='llama-3.3-70b-versatile')
v_log = lg.getLogger(__name__)

"=============================================================================="
l_mensagens = []
l_documents = []
l_docs_site = []
l_docs_outs = []

def resposta_bot(l_mensagens, l_documents):
  mensagem_system = '''Você é um assistente amigável chamado Salin e 
  tem acesso as seguinte informações para dar as suas respostas: {docs_site}'''
  v_template_msg = [('system', mensagem_system)]
  v_template_msg += l_mensagens
  v_template = ChatPromptTemplate.from_messages(v_template_msg )
 
  v_chain = v_template | v_model_chat
  return v_chain.invoke({'docs_site': l_documents}).content

def carrega_site():
  v_loader_docs = WebBaseLoader("https://salinexpress.com.br/")
  l_docs_site = v_loader_docs.load()
  v_local_docs = ''
  for po in l_docs_site:
    v_local_docs += po.page_content
  return v_local_docs

def carrega_pdf():
  v_local_pdfs = '\system-assistant-\datasets'
  return v_local_pdfs

"=============================================================================="
print('Bem-vindo ao ChatBot da Salin! (Digite x quando você quiser sair!)\n')

while True:
  v_pergunta = input('Usuario: ')
  if v_pergunta.lower() == 'x':
    break
  l_documents = carrega_site()
  l_mensagens.append(('user', v_pergunta))
  v_resposta = resposta_bot(l_mensagens, l_documents)
  l_mensagens.append(('assistant', v_resposta))
  print(f'Bot: {v_resposta}')

print('Muito obrigado por usar a Salin Assistente!')
