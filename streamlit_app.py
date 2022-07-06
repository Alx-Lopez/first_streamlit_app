import streamlit
import requests
import snowflake.connector
from urllib.error import URLError

fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+ 'kiwi')

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

def get_fruit(fruit):
    fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+fruit)
    fruit_normalized = pandas.json_normalize(fruityvice_response.json())
    return streamlit.dataframe(fruit_normalized)

try:
    fruit_choice = streamlit.text_input('What fruit would you like information about?')
    if not fruit_choice:
        streamlit.error("Please select a fruit to get information")
    else:
        get_fruit(fruit_choice)
except URLError as e:
    streamlit.error()


def get_fruit_list():
    my_cur = my_cnx.cursor()
    my_cur.execute("select * from fruit_load_list")
    return my_cur.fetchall()


if streamlit.button('Get Fruit Load list'):
    my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
    my_data_row = get_fruit_list()
    my_cnx.close()
    streamlit.dataframe(my_data_row)

add_fruit = streamlit.text_input('What fruit would you like to add?')
def add_fruit_to_list(new_fruit):
    my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
    my_cur = my_cnx.cursor()
    my_cur.execute("insert into fruit_load_list values ('" + new_fruit + "')" )
    my_cnx.close()
    return 'Thanks for adding' + new_fruit
add_fruit_to_list(add_fruit)