import json
import re
from itertools import combinations
import streamlit as st
from connection import iniciar, dados_base
from EndPoints_Structure_Tables import post_new_info, extrair_inf_sys, buscar_tabelas_por_coluna

if __name__ == "__main__":
    st.title("Chatbot Kwai")
    iniciar_objs = iniciar()
    entrada = st.text_input("Digite o que deseja saber:", "")
    extrair_inf_sys(entrada,"1",iniciar_objs[2])
    buscar_tabelas_por_coluna(entrada, iniciar_objs[2])
    post_new_info(entrada,iniciar_objs[2])
