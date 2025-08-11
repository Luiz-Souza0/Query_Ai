import streamlit as st
from pyvis.network import Network
import streamlit.components.v1 as components

def construir_grafo_tabelas_e_relacoes(documentos):
    net = Network(height="600px", width="100%", bgcolor="#ffffff", font_color="black", directed=True)
    net.barnes_hut()

    tabelas = set()
    colunas_por_tabela = {}

    for doc in documentos:
        if "Coluna" in doc and "Tipo" in doc:
            tabela = doc["Tabela"]
            coluna = doc["Coluna"]
            tipo = doc["Tipo"]
            tabelas.add(tabela)
            colunas_por_tabela.setdefault(tabela, []).append((coluna, tipo))

        elif "Coluna_FK" in doc and "Tabela_Referencia" in doc:
            tabelas.add(doc["Tabela"])
            tabelas.add(doc["Tabela_Referencia"])

    for tabela in tabelas:
        net.add_node(tabela, label=tabela, shape="box", color="#1f77b4",font={"size": 20},size=40)

    for tabela, colunas in colunas_por_tabela.items():
        for coluna, tipo in colunas:
            nome_coluna = f"{tabela}.{coluna}"
            net.add_node(nome_coluna, label=f"{coluna} ({tipo})", shape="dot", color="#2ca02c",font={"size": 20},size=40)
            net.add_edge(tabela, nome_coluna)

    for doc in documentos:
        if "Coluna_FK" in doc and "Tabela_Referencia" in doc:
            origem = doc["Tabela"]
            destino = doc["Tabela_Referencia"]
            coluna_fk = doc["Coluna_FK"]
            coluna_ref = doc["Coluna_Referencia"]
            label = f"{origem}.{coluna_fk} → {destino}.{coluna_ref}"
            net.add_edge(origem, destino, label=label, color="#d62728", arrows="to")

    # Salvar num arquivo temporário local
    path = "grafo_tabelas.html"
    net.save_graph(path)
    return path

def tela_estrutura():
    st.set_page_config(page_title="Visualizar Estrutura", layout="wide")
    st.title("📊 Estrutura do Banco de Dados")
    
    st.write("Visualize a estrutura do banco de dados e as relações entre tabelas e colunas.")
    st.write(list(st.session_state.colecao.find({})))
    if "colecao" not in st.session_state:
        st.warning("Conexão com o banco não inicializada. Volte à página principal.")
    else:
        if st.button("Gerar Grafo"):
            if documentos:
                st.success(f"{len(documentos)} documentos carregados.")
                grafo_path = construir_grafo_tabelas_e_relacoes(documentos)
                with open(grafo_path, "r", encoding="utf-8") as f:
                    html_string = f.read()

                # Corrigir largura e altura do container do pyvis
                html_string = html_string.replace("height: 100%;", "height: 100vh;").replace("width: 100%;", "width: 100vw;")

                components.html(html_string, height=800, scrolling=True)

            else:
                st.warning("Nenhum dado encontrado.")
