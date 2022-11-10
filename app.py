import streamlit as st
from wallet_connect import wallet_connect


login_button = wallet_connect(label="login", key="login", message="Login", auth_nft_contract_address="0x68085453B798adf9C09AD8861e0F0da96B908d81")

if login_button == True:
    st.write("Logged in!")
    st.image("dog.jpeg")
else:
    st.write("Not authorized to access this application.")