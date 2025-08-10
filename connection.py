from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

def connection():
    uri = "mongodb+srv://kwai:kwai@cluster0.yzu8jgi.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
    try:
        client = MongoClient(uri, server_api=ServerApi('1'))
        client.admin.command('ping')
        print("Pinged your deployment. You successfully connected to MongoDB!")
        return client
    except Exception as e:
        print(e)
        return None

def dados_base(colecao):
    documentos = list(colecao.find())
    return documentos

def iniciar():
    client = connection()
    if client:
        database = client["base"]
        colecao = database["colecao"]
        return client, database, colecao
    else:
        return None, None, None
