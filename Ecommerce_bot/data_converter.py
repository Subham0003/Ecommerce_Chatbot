import pandas as pd
from langchain_core.documents import Document

def data_converter():

    #read the data
    product_data = pd.read_csv("C:/Users/lenovo/Ecommerce_Chatbot/Ecommerce_Chatbot/data/flipkart_product_review.csv")

    data = product_data[["product_title", "review"]]

    product_list = []

    for _, row in data.iterrows():
        obj = {
            "product_name" : row['product_title'],
            'review' : row['review']
        }
        product_list.append(obj)