import streamlit as st
from wallet_connect import wallet_connect


### ACCESS CONTROL WITH EXISTING NFTS AND TOKENS

#### choose which token you want to use for access control and uncomment the appropriate line
# login_button_erc1155 = wallet_connect(label="login", key="login", message="Login with ERC1155", auth_token_contract_address="0x68085453B798adf9C09AD8861e0F0da96B908d81", chain_name="polygon", contract_type="ERC1155", num_tokens="0")
# login_button_erc721 = wallet_connect(label="login", key="login", message="Login with ERC721", auth_token_contract_address="0x1e988ba4692e52Bc50b375bcC8585b95c48AaD77", chain_name="ethereum", contract_type="ERC721", num_tokens="0")
# login_button_erc20 = wallet_connect(label="login", key="login", message="Login with ERC20", auth_token_contract_address="0x967da4048cD07aB37855c090aAF366e4ce1b9F48", chain_name="ethereum", contract_type="ERC20", num_tokens="20")


### ACCESS CONTROL WITH CUSTOM ALGOVERA NFTS

#### uncomment this and run the app to initialize a new token (take note of the returned tokenId)
button = wallet_connect(message="Create Token", label="create_token", key="create_token", price="0.01", supply=1000, uri="https://gateway.pinata.cloud/ipfs/QmZrFfBGmUmXYUVeTrKdKC1aFeBBEEXQPGhsJtX45GwCC5", chain_name="goerli")
st.write(f"TokenId is {button}")

#### specify the tokenId from above and uncomment for custom Algovera NFT access control
mint_button = wallet_connect(message="Login Algovera", label="mint_and_login_algovera", key="mint_and_login_algovera", price="0.01", token_id="1", chain_name="goerli")

#### make sure you're using the same login_button / mint_button that you've uncommented above
if mint_button == True: # change to login_button_erc1155 / login_button_erc721 / login_button_erc20 / mint_button if appropriate
    st.write("Logged in!")
    st.image("dog.jpeg")
else:
    st.write("Not authorized to access this application.")
