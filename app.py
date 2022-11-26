import streamlit as st
from wallet_connect import wallet_connect


# login_button_erc1155 = wallet_connect(label="login", key="login", message="Login with ERC1155", auth_token_contract_address="0x68085453B798adf9C09AD8861e0F0da96B908d81", chain_name="polygon", contract_type="ERC1155", num_tokens="0")
# login_button_erc721 = wallet_connect(label="login", key="login", message="Login with ERC721", auth_token_contract_address="0x1e988ba4692e52Bc50b375bcC8585b95c48AaD77", chain_name="ethereum", contract_type="ERC721", num_tokens="0")
login_button_erc20 = wallet_connect(label="login", key="login", message="Login with ERC20", auth_token_contract_address="0x967da4048cD07aB37855c090aAF366e4ce1b9F48", chain_name="ethereum", contract_type="ERC20", num_tokens="20")

if login_button_erc20 == True:
    st.write("Logged in!")
    st.image("dog.jpeg")
else:
    st.write("Not authorized to access this application.")