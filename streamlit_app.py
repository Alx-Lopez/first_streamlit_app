import streamlit

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
streamlit.dataframe(fruit_list)