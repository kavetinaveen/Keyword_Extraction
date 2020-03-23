import streamlit as st
import RAKE
import altair as alt
import pandas as pd

stop_dir = "SmartStoplist.txt"
rake_object = RAKE.Rake(stop_dir)
title = st.text_input('Enter your input text here...', '')
if title != '':
	keywords = rake_object.run(title)
	keywords = pd.DataFrame(keywords, columns = ['Key Phrase', 'Score'])
	keywords = keywords[:5]
	st.write('Keywords (or phrases):')
	st.table(keywords)