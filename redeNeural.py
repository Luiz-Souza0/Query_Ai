import json
import re
from itertools import combinations
import streamlit as st
import streamlit.components.v1 as components
from connection import iniciar, dados_base
from EndPoints_Structure_Tables import post_new_info, extrair_inf_sys, buscar_tabelas_por_coluna
from pages.listagemdatabase import tela_estrutura

# Código do Google AdSense (adicionando o script)
adsense_script = """
<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-2048026353757692" 
     crossorigin="anonymous"></script>
"""

# Adicionando a metatag para a conta do AdSense
adsense_metatag = """
<meta name="google-adsense-account" content="ca-pub-2048026353757692">
"""

# Adicionando o anúncio (com seu slot de anúncio)
adsense_snippet = """
<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-2048026353757692"
     crossorigin="anonymous"></script>
<!-- teste -->
<ins class="adsbygoogle"
     style="display:block"
     data-ad-client="ca-pub-2048026353757692"
     data-ad-slot="6400059606"
     data-ad-format="auto"
     data-full-width-responsive="true"></ins>
<script>
     (adsbygoogle = window.adsbygoogle || []).push({});
</script>
"""

# Inserir os scripts do AdSense no Streamlit
components.html(adsense_script, height=0)
components.html(adsense_metatag, height=0)

# Adicionando o anúncio na página
components.html(
    adsense_snippet,
    height=100
)

# Seu código do Streamlit continua aqui
iniciar_objs = iniciar()

# Initialization
if 'colecao' not in st.session_state:
    st.session_state['colecao'] = iniciar_objs[2]

if __name__ == "__main__":
    st.set_page_config( page_title="ChatBot", page_icon=":heavy_plus_sign:" )
    
    # Paginação ou outras configurações podem ser adicionadas
    # pagina = st.sidebar.selectbox("📚 Navegação", ["Chatbot", "Estrutura"])

    # Caso o usuário vá para "Chatbot"
    st.title("Chatbot")
    entrada = st.text_input("Digite o que deseja saber:", "")
    extrair_inf_sys(entrada,"1",st.session_state.colecao)
    buscar_tabelas_por_coluna(entrada, st.session_state.colecao)
    post_new_info(entrada,st.session_state.colecao)

    # Caso precise de outras opções como "Estrutura"
    # elif pagina == "Estrutura":
    #     tela_estrutura()
