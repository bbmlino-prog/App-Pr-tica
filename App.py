import streamlit as st
from streamlit_option_menu import option_menu

st.header("Introduzindo os elementos do Streamlit") 

menu = option_menu(menu_title="Menu",
                   options=["início", "Gráficos Estatísticos", "Gráfico Dinámicos", "Widgets", "Formulários",]
                   Icons=["house", "bar-chart", "bar-chart-line", "toggles", "bar-chart",]
                   Menu_icon="cast",
                   defaut_index=o,
                   orientation="horizontal"
)
