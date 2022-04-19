import pandas as pd
import numpy as np
import streamlit as st
from datetime import time, datetime

# https://share.streamlit.io/streamlit/30days

st.header('Line chart')

chart_data = pd.DataFrame(np.random.randn(20, 3), columns=['a', 'b', 'c'])

st.line_chart(chart_data)