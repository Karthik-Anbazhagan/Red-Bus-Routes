import pandas as pd
import pymysql
import streamlit as slt
from streamlit_option_menu import option_menu
#import plotly.express as px
import time

#kerala bus
lists_K=[]
df_K=pd.read_csv("df_buses_Kerala_1.csv")
for i,r in df_K.iterrows():
    lists_K.append(r["Route_names"])

#Andra bus
lists_A=[]
df_A=pd.read_csv("df_buses_Andra_2.csv")
for i,r in df_A.iterrows():
    lists_A.append(r["Route_names"])
#Telugana bus
lists_T=[]
df_T=pd.read_csv("df_buses_Telugana_3.csv")
for i,r in df_T.iterrows():
    lists_T.append(r["Route_names"])
#Goa bus
lists_G=[]
df_G=pd.read_csv("df_buses_Goa_4.csv")
for i,r in df_G.iterrows():
    lists_G.append(r["Route_names"])
#Rajastan bus
lists_R=[]
df_R=pd.read_csv("df_buses_Rajastan_5.csv")
for i,r in df_R.iterrows():
    lists_R.append(r["Route_names"])
#South Bengal bus
lists_SB=[]
df_SB=pd.read_csv("df_buses_South_bengal_6.csv")
for i,r in df_SB.iterrows():
    lists_SB.append(r["Route_names"])
#Haryana bus
lists_H=[]
df_H=pd.read_csv("df_buses_Haryana_7.csv")
for i,r in df_H.iterrows():
    lists_H.append(r["Route_names"])
#Assam bus
lists_AS=[]
df_AS=pd.read_csv("df_buses_Assam_8.csv")
for i,r in df_AS.iterrows():
    lists_AS.append(r["Route_names"])
#Uttra Pradesh bus
lists_UP=[]
df_UP=pd.read_csv("df_buses_Uttra_pradesh_9.csv")
for i,r in df_UP.iterrows():
    lists_UP.append(r["Route_names"])
#West bengalbus
lists_WB=[]
df_WB=pd.read_csv("df_buses_West_bengal_10.csv")
for i,r in df_WB.iterrows():
    lists_WB.append(r["Route_names"])


#setting up streamlit page
slt.set_page_config(layout="wide")

web=option_menu(menu_title="OnlineBus",
                options=["Home", "States and Routes"],
                icons=["house", "info-circle"],
                orientation="horizontal"
                )

#Home page setting
if web=="Home":
    #slt.image("t_500x300.jpg",width=200)
    slt.title("Redbus Data Scraping with Selenium & Dynamic Filtering using Streamlit")
    slt.subheader(":red[Domain:] Bus Transportation")
    slt.subheader(":red[Ojective:]")
    slt.markdown("The Redbus Data Scraping and Filtering with streamlit Application aims to enhance the experience of travelers and bus service providers by scraping bus route data from the popular transportation platform.")
    slt.subheader(":red[Overview:]")
    slt.markdown("Selenium: Selenium is a library used for automating web browser. It is commonly used for web scraping, which involves extracting data from websites.")
    slt.markdown('''Pandas: Use the powerful Pandas library to transform the dataset from CSV format into a structured dataframe
                Pandas helps data manipulation, cleaning and preprocessing, ensuring that data was ready for analysis.''')
    slt.markdown('''MySQL: With help of sql to establish a connection to a SQL database, enabling seamless intergration of the transformed dataset
                and the data was efficiently inserted into relevent tables for storage and retrieval.''')
    slt.markdown("Streamlit: Developed an interactive web application using Streamlit, a user-friendly framework for data visualization and analysis.")
    slt.subheader(":blue[Skill-take:]")
    slt.markdown("Selenium, Python, Pandas, MySQL, Streamlit.")
    slt.subheader(":blue[Developed-by:] Karthik Anbazhagan")

#States and Routes page Setting
if web=="States and Routes":
    S = slt.selectbox("Lists of states",["Kerala", "Andhra Pradesh", "Telugana", "Goa",
                                    "Rajastan", "South Bengal", "Haryana", "Assam", "Uttra Pradesh", "West Bengal"])
    select_fare = slt.radio("Sort by: Price: Low-High", ("50-1000", "1000-2000", "2000 and above"))
#Kerala bus fare filtering
    if S == "Kerala":
        K = slt.selectbox("list of routes", lists_K)

        if select_fare=="50-1000":
            conn=pymysql.connect(host="localhost", user="root", password="12345", database="red_bus")
            my_cursor = conn.cursor()
            query=f'''select * from bus_details
                            where Price Between 50 and 1000 and Route_names="{K}"
                            order by Price desc'''
            my_cursor.execute(query)
            out=my_cursor.fetchall()
            df=pd.DataFrame(out,columns=["ID", "Bus_name", "Bus_type", "Departing_time", "Reaching_time", "Duration",
                                    "Price", "Seat_availabe", "Rating", "Route_links", "Route_names"])
            slt.write(df)
        if select_fare=="1000-2000":
            conn=pymysql.connect(host="localhost", user="root", password="12345", database="RED_BUS_ROUTES")
            my_cursor = conn.cursor()
            query=f'''select * from bus_details
                            where Price Between 1000 and 2000 and Route_names="{K}"
                            order by Price desc'''
            my_cursor.execute(query)
            out=my_cursor.fetchall()
            df=pd.DataFrame(out,columns=["ID", "Bus_name", "Bus_type", "Departing_time", "Reaching_time", "Duration",
                                    "Price", "Seat_availabe", "Rating", "Route_links", "Route_names"])
            slt.write(df)
        if select_fare=="2000 and above":
            conn=pymysql.connect(host="localhost", user="root", password="12345", database="RED_BUS_ROUTES")
            my_cursor = conn.cursor()
            query=f'''select * from bus_details
                            where Price > 2000 and Route_names="{K}"
                            order by Price desc'''
            my_cursor.execute(query)
            out=my_cursor.fetchall()
            df=pd.DataFrame(out,columns=["ID", "Bus_name", "Bus_type", "Departing_time", "Reaching_time", "Duration",
                                    "Price", "Seat_availabe", "Rating", "Route_links", "Route_names"])
            slt.write(df)
#Andhra Pradesh bus fare filering
    if S == "Andhra Pradesh":
        A = slt.selectbox("list of routes", lists_A)

        if select_fare=="50-1000":
            conn=pymysql.connect(host="localhost", user="root", password="12345", database="RED_BUS_ROUTES")
            my_cursor = conn.cursor()
            query=f'''select * from bus_details
                            where Price Between 50 and 1000 and Route_names="{A}"
                            order by Price desc'''
            my_cursor.execute(query)
            out=my_cursor.fetchall()
            df=pd.DataFrame(out,columns=["ID", "Bus_name", "Bus_type", "Departing_time", "Reaching_time", "Duration",
                                    "Price", "Seat_availabe", "Rating", "Route_links", "Route_names"])
            slt.write(df)
        if select_fare=="1000-2000":
            conn=pymysql.connect(host="localhost", user="root", password="12345", database="RED_BUS_ROUTES")
            my_cursor = conn.cursor()
            query=f'''select * from bus_details
                            where Price Between 1000 and 2000 and Route_names="{A}"
                            order by Price desc'''
            my_cursor.execute(query)
            out=my_cursor.fetchall()
            df=pd.DataFrame(out,columns=["ID", "Bus_name", "Bus_type", "Departing_time", "Reaching_time", "Duration",
                                    "Price", "Seat_availabe", "Rating", "Route_links", "Route_names"])
            slt.write(df)
        if select_fare=="2000 and above":
            conn=pymysql.connect(host="localhost", user="root", password="12345", database="RED_BUS_ROUTES")
            my_cursor = conn.cursor()
            query=f'''select * from bus_details
                            where Price > 2000 and Route_names="{A}"
                            order by Price desc'''
            my_cursor.execute(query)
            out=my_cursor.fetchall()
            df=pd.DataFrame(out,columns=["ID", "Bus_name", "Bus_type", "Departing_time", "Reaching_time", "Duration",
                                    "Price", "Seat_availabe", "Rating", "Route_links", "Route_names"])
            slt.write(df)
#Telugana bus fare filtering
    if S == "Telugana":
        T = slt.selectbox("list of routes", lists_T)

        if select_fare=="50-1000":
            conn=pymysql.connect(host="localhost", user="root", password="12345", database="RED_BUS_ROUTES")
            my_cursor = conn.cursor()
            query=f'''select * from bus_details
                            where Price Between 50 and 1000 and Route_names="{T}"
                            order by Price desc'''
            my_cursor.execute(query)
            out=my_cursor.fetchall()
            df=pd.DataFrame(out,columns=["ID", "Bus_name", "Bus_type", "Departing_time", "Reaching_time", "Duration",
                                    "Price", "Seat_availabe", "Rating", "Route_links", "Route_names"])
            slt.write(df)
        if select_fare=="1000-2000":
            conn=pymysql.connect(host="localhost", user="root", password="12345", database="RED_BUS_ROUTES")
            my_cursor = conn.cursor()
            query=f'''select * from bus_details
                            where Price Between 1000 and 2000 and Route_names="{T}"
                            order by Price desc'''
            my_cursor.execute(query)
            out=my_cursor.fetchall()
            df=pd.DataFrame(out,columns=["ID", "Bus_name", "Bus_type", "Departing_time", "Reaching_time", "Duration",
                                    "Price", "Seat_availabe", "Rating", "Route_links", "Route_names"])
            slt.write(df)
        if select_fare=="2000 and above":
            conn=pymysql.connect(host="localhost", user="root", password="12345", database="RED_BUS_ROUTES")
            my_cursor = conn.cursor()
            query=f'''select * from bus_details
                            where Price > 2000 and Route_names="{T}"
                            order by Price desc'''
            my_cursor.execute(query)
            out=my_cursor.fetchall()
            df=pd.DataFrame(out,columns=["ID", "Bus_name", "Bus_type", "Departing_time", "Reaching_time", "Duration",
                                    "Price", "Seat_availabe", "Rating", "Route_links", "Route_names"])
            slt.write(df)
#Goa bus fare filtering
    if S == "Goa":
        G = slt.selectbox("list of routes", lists_G)

        if select_fare=="50-1000":
            conn=pymysql.connect(host="localhost", user="root", password="12345", database="RED_BUS_ROUTES")
            my_cursor = conn.cursor()
            query=f'''select * from bus_details
                            where Price Between 50 and 1000 and Route_names="{G}"
                            order by Price desc'''
            my_cursor.execute(query)
            out=my_cursor.fetchall()
            df=pd.DataFrame(out,columns=["ID", "Bus_name", "Bus_type", "Departing_time", "Reaching_time", "Duration",
                                    "Price", "Seat_availabe", "Rating", "Route_links", "Route_names"])
            slt.write(df)
        if select_fare=="1000-2000":
            conn=pymysql.connect(host="localhost", user="root", password="12345", database="RED_BUS_ROUTES")
            my_cursor = conn.cursor()
            query=f'''select * from bus_details
                            where Price Between 1000 and 2000 and Route_names={G}"
                            order by Price desc'''
            my_cursor.execute(query)
            out=my_cursor.fetchall()
            df=pd.DataFrame(out,columns=["ID", "Bus_name", "Bus_type", "Departing_time", "Reaching_time", "Duration",
                                    "Price", "Seat_availabe", "Rating", "Route_links", "Route_names"])
            slt.write(df)
        if select_fare=="2000 and above":
            conn=pymysql.connect(host="localhost", user="root", password="12345", database="RED_BUS_ROUTES")
            my_cursor = conn.cursor()
            query=f'''select * from bus_details
                            where Price > 2000 and Route_names="{G}"
                            order by Price desc'''
            my_cursor.execute(query)
            out=my_cursor.fetchall()
            df=pd.DataFrame(out,columns=["ID", "Bus_name", "Bus_type", "Departing_time", "Reaching_time", "Duration",
                                    "Price", "Seat_availabe", "Rating", "Route_links", "Route_names"])
            slt.write(df)
#Rajastan Bus fare filtering
    if S == "Rajastan":
        R = slt.selectbox("list of routes", lists_R)

        if select_fare=="50-1000":
            conn=pymysql.connect(host="localhost", user="root", password="12345", database="RED_BUS_ROUTES")
            my_cursor = conn.cursor()
            query=f'''select * from bus_details
                            where Price Between 50 and 1000 and Route_names="{R}"
                            order by Price desc'''
            my_cursor.execute(query)
            out=my_cursor.fetchall()
            df=pd.DataFrame(out,columns=["ID", "Bus_name", "Bus_type", "Departing_time", "Reaching_time", "Duration",
                                    "Price", "Seat_availabe", "Rating", "Route_links", "Route_names"])
            slt.write(df)
        if select_fare=="1000-2000":
            conn=pymysql.connect(host="localhost", user="root", password="12345", database="RED_BUS_ROUTES")
            my_cursor = conn.cursor()
            query=f'''select * from bus_details
                            where Price Between 1000 and 2000 and Route_names="{R}"
                            order by Price desc'''
            my_cursor.execute(query)
            out=my_cursor.fetchall()
            df=pd.DataFrame(out,columns=["ID", "Bus_name", "Bus_type", "Departing_time", "Reaching_time", "Duration",
                                    "Price", "Seat_availabe", "Rating", "Route_links", "Route_names"])
            slt.write(df)
        if select_fare=="2000 and above":
            conn=pymysql.connect(host="localhost", user="root", password="12345", database="RED_BUS_ROUTES")
            my_cursor = conn.cursor()
            query=f'''select * from bus_details
                            where Price > 2000 and Route_names="{R}"
                            order by Price desc'''
            my_cursor.execute(query)
            out=my_cursor.fetchall()
            df=pd.DataFrame(out,columns=["ID", "Bus_name", "Bus_type", "Departing_time", "Reaching_time", "Duration",
                                    "Price", "Seat_availabe", "Rating", "Route_links", "Route_names"])
            slt.write(df)
#South Bengal bus fare Filtering
    if S == "South Bengal":
        SB = slt.selectbox("list of routes", lists_SB)

        if select_fare=="50-1000":
            conn=pymysql.connect(host="localhost", user="root", password="12345", database="RED_BUS_ROUTES")
            my_cursor = conn.cursor()
            query=f'''select * from bus_details
                            where Price Between 50 and 1000 and Route_names="[{SB}"
                            order by Price desc'''
            my_cursor.execute(query)
            out=my_cursor.fetchall()
            df=pd.DataFrame(out,columns=["ID", "Bus_name", "Bus_type", "Departing_time", "Reaching_time", "Duration",
                                    "Price", "Seat_availabe", "Rating", "Route_links", "Route_names"])
            slt.write(df)
        if select_fare=="1000-2000":
            conn=pymysql.connect(host="localhost", user="root", password="12345", database="RED_BUS_ROUTES")
            my_cursor = conn.cursor()
            query=f'''select * from bus_details
                            where Price Between 1000 and 2000 and Route_names="{SB}"
                            order by Price desc'''
            my_cursor.execute(query)
            out=my_cursor.fetchall()
            df=pd.DataFrame(out,columns=["ID", "Bus_name", "Bus_type", "Departing_time", "Reaching_time", "Duration",
                                    "Price", "Seat_availabe", "Rating", "Route_links", "Route_names"])
            slt.write(df)
        if select_fare=="2000 and above":
            conn=pymysql.connect(host="localhost", user="root", password="12345", database="RED_BUS_ROUTES")
            my_cursor = conn.cursor()
            query=f'''select * from bus_details
                            where Price > 2000 and Route_names="{SB}"
                            order by Price desc'''
            my_cursor.execute(query)
            out=my_cursor.fetchall()
            df=pd.DataFrame(out,columns=["ID", "Bus_name", "Bus_type", "Departing_time", "Reaching_time", "Duration",
                                    "Price", "Seat_availabe", "Rating", "Route_links", "Route_names"])
            slt.write(df)
#Haryana bus fare filtering
    if S == "Haryana":
        H = slt.selectbox("list of routes", lists_H)

        if select_fare=="50-1000":
            conn=pymysql.connect(host="localhost", user="root", password="12345", database="RED_BUS_ROUTES")
            my_cursor = conn.cursor()
            query=f'''select * from bus_details
                            where Price Between 50 and 1000 and Route_names="{H}"
                            order by Price desc'''
            my_cursor.execute(query)
            out=my_cursor.fetchall()
            df=pd.DataFrame(out,columns=["ID", "Bus_name", "Bus_type", "Departing_time", "Reaching_time", "Duration",
                                    "Price", "Seat_availabe", "Rating", "Route_links", "Route_names"])
            slt.write(df)
        if select_fare=="1000-2000":
            conn=pymysql.connect(host="localhost", user="root", password="12345", database="RED_BUS_ROUTES")
            my_cursor = conn.cursor()
            query=f'''select * from bus_details
                            where Price Between 1000 and 2000 and Route_names="{H}"
                            order by Price desc'''
            my_cursor.execute(query)
            out=my_cursor.fetchall()
            df=pd.DataFrame(out,columns=["ID", "Bus_name", "Bus_type", "Departing_time", "Reaching_time", "Duration",
                                    "Price", "Seat_availabe", "Rating", "Route_links", "Route_names"])
            slt.write(df)
        if select_fare=="2000 and above":
            conn=pymysql.connect(host="localhost", user="root", password="12345", database="RED_BUS_ROUTES")
            my_cursor = conn.cursor()
            query=f'''select * from bus_details
                            where Price > 2000 and Route_names="{H}"
                            order by Price desc'''
            my_cursor.execute(query)
            out=my_cursor.fetchall()
            df=pd.DataFrame(out,columns=["ID", "Bus_name", "Bus_type", "Departing_time", "Reaching_time", "Duration",
                                    "Price", "Seat_availabe", "Rating", "Route_links", "Route_names"])
            slt.write(df)
#Assam bus fare filtering 
    if S == "Assam":
        AS = slt.selectbox("list of routes", lists_AS)

        if select_fare=="50-1000":
            conn=pymysql.connect(host="localhost", user="root", password="12345", database="RED_BUS_ROUTES")
            my_cursor = conn.cursor()
            query=f'''select * from bus_details
                            where Price Between 50 and 1000 and Route_names="{AS}"
                            order by Price desc'''
            my_cursor.execute(query)
            out=my_cursor.fetchall()
            df=pd.DataFrame(out,columns=["ID", "Bus_name", "Bus_type", "Departing_time", "Reaching_time", "Duration",
                                    "Price", "Seat_availabe", "Rating", "Route_links", "Route_names"])
            slt.write(df)
        if select_fare=="1000-2000":
            conn=pymysql.connect(host="localhost", user="root", password="12345", database="RED_BUS_ROUTES")
            my_cursor = conn.cursor()
            query=f'''select * from bus_details
                            where Price Between 1000 and 2000 and Route_names="{AS}"
                            order by Price desc'''
            my_cursor.execute(query)
            out=my_cursor.fetchall()
            df=pd.DataFrame(out,columns=["ID", "Bus_name", "Bus_type", "Departing_time", "Reaching_time", "Duration",
                                    "Price", "Seat_availabe", "Rating", "Route_links", "Route_names"])
            slt.write(df)
        if select_fare=="2000 and above":
            conn=pymysql.connect(host="localhost", user="root", password="12345", database="RED_BUS_ROUTES")
            my_cursor = conn.cursor()
            query=f'''select * from bus_details
                            where Price > 2000 and Route_names="{AS}"
                            order by Price desc'''
            my_cursor.execute(query)
            out=my_cursor.fetchall()
            df=pd.DataFrame(out,columns=["ID", "Bus_name", "Bus_type", "Departing_time", "Reaching_time", "Duration",
                                    "Price", "Seat_availabe", "Rating", "Route_links", "Route_names"])
            slt.write(df)
#Uttra Pradesh bus fare filtering
    if S == "Uttra Pradesh":
        UP = slt.selectbox("list of routes", lists_UP)

        if select_fare=="50-1000":
            conn=pymysql.connect(host="localhost", user="root", password="12345", database="RED_BUS_ROUTES")
            my_cursor = conn.cursor()
            query=f'''select * from bus_details
                            where Price Between 50 and 1000 and Route_names="{UP}"
                            order by Price desc'''
            my_cursor.execute(query)
            out=my_cursor.fetchall()
            df=pd.DataFrame(out,columns=["ID", "Bus_name", "Bus_type", "Departing_time", "Reaching_time", "Duration",
                                    "Price", "Seat_availabe", "Rating", "Route_links", "Route_names"])
            slt.write(df)
        if select_fare=="1000-2000":
            conn=pymysql.connect(host="localhost", user="root", password="12345", database="RED_BUS_ROUTES")
            my_cursor = conn.cursor()
            query=f'''select * from bus_details
                            where Price Between 1000 and 2000 and Route_names="{UP}"
                            order by Price desc'''
            my_cursor.execute(query)
            out=my_cursor.fetchall()
            df=pd.DataFrame(out,columns=["ID", "Bus_name", "Bus_type", "Departing_time", "Reaching_time", "Duration",
                                    "Price", "Seat_availabe", "Rating", "Route_links", "Route_names"])
            slt.write(df)
        if select_fare=="2000 and above":
            conn=pymysql.connect(host="localhost", user="root", password="12345", database="RED_BUS_ROUTES")
            my_cursor = conn.cursor()
            query=f'''select * from bus_details
                            where Price > 2000 and Route_names="{UP}"
                            order by Price desc'''
            my_cursor.execute(query)
            out=my_cursor.fetchall()
            df=pd.DataFrame(out,columns=["ID", "Bus_name", "Bus_type", "Departing_time", "Reaching_time", "Duration",
                                    "Price", "Seat_availabe", "Rating", "Route_links", "Route_names"])
            slt.write(df)
#West Bengal Bus fare Filtering
    if S == "West Bengal":
        WB = slt.selectbox("list of routes", lists_WB)

        if select_fare=="50-1000":
            conn=pymysql.connect(host="localhost", user="root", password="12345", database="RED_BUS_ROUTES")
            my_cursor = conn.cursor()
            query=f'''select * from bus_details
                            where Price Between 50 and 1000 and Route_names="{WB}"
                            order by Price desc'''
            my_cursor.execute(query)
            out=my_cursor.fetchall()
            df=pd.DataFrame(out,columns=["ID", "Bus_name", "Bus_type", "Departing_time", "Reaching_time", "Duration",
                                    "Price", "Seat_availabe", "Rating", "Route_links", "Route_names"])
            slt.write(df)
        if select_fare=="1000-2000":
            conn=pymysql.connect(host="localhost", user="root", password="12345", database="RED_BUS_ROUTES")
            my_cursor = conn.cursor()
            query=f'''select * from bus_details
                            where Price Between 1000 and 2000 and Route_names="{WB}"
                            order by Price desc'''
            my_cursor.execute(query)
            out=my_cursor.fetchall()
            df=pd.DataFrame(out,columns=["ID", "Bus_name", "Bus_type", "Departing_time", "Reaching_time", "Duration",
                                    "Price", "Seat_availabe", "Rating", "Route_links", "Route_names"])
            slt.write(df)
        if select_fare=="2000 and above":
            conn=pymysql.connect(host="localhost", user="root", password="12345", database="RED_BUS_ROUTES")
            my_cursor = conn.cursor()
            query=f'''select * from bus_details
                            where Price > 2000 and Route_names="{WB}"
                            order by Price desc'''
            my_cursor.execute(query)
            out=my_cursor.fetchall()
            df=pd.DataFrame(out,columns=["ID", "Bus_name", "Bus_type", "Departing_time", "Reaching_time", "Duration",
                                    "Price", "Seat_availabe", "Rating", "Route_links", "Route_names"])
            slt.write(df)