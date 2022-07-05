import streamlit
import requests
fq = 'kiwi'
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+fq)

streamlit.title('My Parents New Healthy Diner')

streamlit.header('Breakfast Favorites')

streamlit.text('🍜  Omega 3 and Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔  Hard-Boiled Free-Range Egg')

streamlit.text('🥑 🍞 Avocado Toast')


streamlit.header('Build your own Fruit smoothie ')

import pandas

file_path = 'https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt'
fruit_list = pandas.read_csv(file_path)
fruit_list = fruit_list.set_index('Fruit')

fruits_selected = streamlit.multiselect("Pick some fruits:",list(fruit_list.index),['Avocado','Strawberries'])

filter_fruits = fruit_list.loc[fruits_selected]

streamlit.dataframe(filter_fruits)

streamlit.header('Fruityvice Fruit Advice!')
streamlit.text(fruityvice_response.json())
fruit_normalized = pandas.json_normalize(fruityvice_response.json())
streamlit.dataframe(fruit_normalized)