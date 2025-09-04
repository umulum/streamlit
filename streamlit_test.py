import streamlit as st
import pandas as pd

orders = pd.read_excel("sample_superstore.xls", sheet_name='Orders')
returns = pd.read_excel("sample_superstore.xls", sheet_name='Returns')
people = pd.read_excel("sample_superstore.xls", sheet_name='People')

print(orders.head())
print(orders.info())