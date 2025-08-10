from connection import dados_base
import streamlit as st

def extrair_inf_sys(entrada, id_info, colecao=""):
    entrada = entrada.strip().lower()

    if entrada == "":
        if id_info == "1":
            return st.write("Entrada Vazia!")
        else:
            return ""

    base = dados_base(colecao)

    found = any(
        entrada in str(value).lower()
        for doc in base
        for value in doc.values()
    )
    if id_info == "1":
        return st.write("Resposta:", "found") if found else st.write("Não Encontrado")
    else:
        return "found" if found else "can you tell about it?"

def buscar_tabelas_por_coluna(nome_coluna, colecao):
    nome_coluna = nome_coluna.strip().lower()
    if not nome_coluna:
        return []

    base = dados_base(colecao)  # Busca todos os docs da coleção

    tabelas = {
        doc["Tabela"]
        for doc in base
        if str(doc.get("Coluna", "")).lower() == nome_coluna
    }

    
    if tabelas:
        st.write("Tabelas que possuem a coluna:", list(tabelas))
    else:
        st.write("Nenhuma tabela encontrada com essa coluna.")

def post_new_info(entrada,colecao):
    if extrair_inf_sys(entrada, "2", colecao) == "can you tell about it?":
        st.write("Por favor, forneça mais informações:")
        
        match st.selectbox("qual informação?", ["Coluna X Tabela", "Chave Primária", "Chave Estrangeira"]) :
            case "Coluna X Tabela":
                st.write("Você escolheu Coluna X Tabela.")
                with st.form("ColXTab"):
                    Table = st.text_input("Digite a tabela:")
                    New_Collumn = st.text_input("Digite a coluna:")
                    Collumn_Type = st.selectbox("Qual o tipo da coluna:",["INT", "VARCHAR", "TEXT", "DATE", "BOOLEAN", "FLOAT"])
                                    
                    submitted = st.form_submit_button("Adicionar informação")
                    if submitted:
                        nova_info_dict = {
                            "Tabela": Table,
                            "Coluna": New_Collumn,
                            "Tipo": Collumn_Type
                        }                       
                        try:
                            colecao.insert_one(nova_info_dict)
                            st.success("Informação adicionada com sucesso!")
                        except json.JSONDecodeError:
                            st.error("Por favor, insira um JSON válido.")
                    
                
                        
            case "Chave Primária":
                st.write("Você escolheu Chave Primária.")
                with st.form("ChavePrimaria"):
                    tabela = st.text_input("Digite o nome da tabela:")
                    chave_primaria = st.text_input("Digite o nome da chave primária:")
                    submitted = st.form_submit_button("Adicionar informação")
                    if submitted:
                        nova_info_dict = {
                            "Tabela": tabela,
                            "Chave_Primaria": chave_primaria
                        }
                        try:
                            colecao.insert_one(nova_info_dict)
                            st.success("Chave primária adicionada com sucesso!")
                        except json.JSONDecodeError:
                            st.error("Erro ao inserir a chave primária.")
            
            case "Chave Estrangeira":
                st.write("Você escolheu Chave Estrangeira.")
                with st.form("ChaveEstrangeira"):
                    tabela = st.text_input("Digite o nome da tabela:")
                    coluna_fk = st.text_input("Digite o nome da coluna (chave estrangeira):")
                    tabela_referencia = st.text_input("Digite o nome da tabela de referência:")
                    coluna_referencia = st.text_input("Digite o nome da coluna de referência:")
                    submitted = st.form_submit_button("Adicionar informação")
                    if submitted:
                        nova_info_dict = {
                            "Tabela": tabela,
                            "Coluna_FK": coluna_fk,
                            "Tabela_Referencia": tabela_referencia,
                            "Coluna_Referencia": coluna_referencia
                        }
                        try:
                            colecao.insert_one(nova_info_dict)
                            st.success("Chave estrangeira adicionada com sucesso!")
                        except json.JSONDecodeError:
                            st.error("Erro ao inserir a chave estrangeira.")