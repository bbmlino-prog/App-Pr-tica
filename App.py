import streamlit as st
from streamlit_option_menu import option_menu
import numpy as np
import pandas as pd

st.header("Introduzindo os elementos do Streamlit") 

menu = option_menu(menu_title="Menu",
                   options=["início", "Gráficos Estatísticos", "Gráfico Dinámicos", "Widgets", "Formulários"],
                   icons=["house", "bar-chart", "bar-chart-line", "toggles", "bar-chart"],
                   menu_icon="cast",
                   default_index=0,
                   orientation="horizontal"
)

