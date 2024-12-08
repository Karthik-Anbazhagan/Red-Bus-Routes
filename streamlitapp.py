import pandas as pd
import pymysql
import streamlit as slt
from streamlit_option_menu import option_menu

# kerala bus
lists_K = []
df_K = pd.read_csv("df_buses_Kerala_1.csv")
for i, r in df_K.iterrows():
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

# Function to fetch bus data based on price range and route
def fetch_bus_data(route, fare_range, bus_type, rating_range, departure_start, reaching_end, Seat_available):
    conn = pymysql.connect(host="localhost", user="root", password="12345", database="red_bus")
    my_cursor = conn.cursor()
    
    query='''SELECT * FROM bus_details WHERE Price BETWEEN  %s AND %s AND Route_names = %s and Bus_Type LIKE %s and Star_rating BETWEEN %s
    AND %s AND Departing_time = %s 
    AND Reaching_time = %s AND Seat_available = %s ORDER BY Route_names DESC'''
    
    if fare_range == "50-1000":
        min_price, max_price = 50, 1000
    elif fare_range =="1000-2000":
        min_price, max_price = 1000, 2000
    else:
        min_price, max_price = 2000, 3000
    if rating_range == "0-1":
        min_rating, max_rating = 0, 1.00
    elif rating_range =="1-2":
        min_rating, max_rating = 1.00, 2.00    
    elif rating_range == "2-3":
        min_rating, max_rating = 2.00, 3.00
    elif rating_range == "3-4":
        min_rating, max_rating = 3.00, 4.00    
    else:
        min_rating, max_rating = 4.00, 5.00

    params = (min_price, max_price, route, f"%{bus_type}%", min_rating, max_rating, departure_start, reaching_end, Seat_available)
    my_cursor.execute(query, params)
    out = my_cursor.fetchall()
    conn.close()
    return out    

# Streamlit app page configuration
slt.set_page_config(layout="wide")

# Options menu
web = option_menu(menu_title="OnlineBus",
                options=["Home", "States and Routes"],
                icons=["house", "info-circle"],
                orientation="horizontal")

# Home page setting
if web == "Home":
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

# States and Routes page setting
if web == "States and Routes":
    S = slt.selectbox("Lists of states",["Kerala", "Andhra Pradesh", "Telugana", "Goa",
                                    "Rajastan", "South Bengal", "Haryana", "Assam", "Uttra Pradesh", "West Bengal"])
    select_fare = slt.radio("Sort by: Price: Low-High", ["50-1000", "1000-2000", "2000-3000"])
    bus_type = slt.selectbox("Bus_Type", ["AC Seater", "AC Sleeper", "AC Semi Sleeper", "AC-Seater/Sleeper", 
                                        "Non-AC-Seater", "Non-AC-Sleeper", "Non-AC-Semi-Sleeper", "Non_AC_Seater/Sleeper"])
    Rating = slt.radio("**Rating:** ★★★★☆", ("0-1", "1-2", "3-4", "4-5"))
    Departing_time=slt.selectbox("Departing Time:", ["10:00", "12:00", "13:46", "15:00", "15:25", "16:00", "16:15", "16:45", "19:00", "20:00", "20:40", "21:30", "22:10", "22:30", "23:00", "21:15", "21:45", "04:30", "06:30", "06:40", "07:20", "08:30", "09:00", "09:10", "09:30", "09:35", "10:05", "10:15", "10:55", "12:30", "13:40", "13:50", "13:55", "14:00", "14:31", "20:05", "21:00", "22:00", "23:30", "07:00", "07:30", "08:05", "13:30", "18:00", "19:05", "22:15", "12:15", "20:30", "04:00", "05:00", "05:19", "05:55", "06:34", "07:24", "07:40", "07:54", "08:54", "09:54", "10:02", "13:20", "13:25", "13:34", "14:59", "16:30", "16:55", "16:59", "19:30", "20:45", "20:50", "20:55", "06:02", "07:01", "12:02", "12:50", "14:01", "14:46", "14:50", "15:45", "16:20", "17:00", "17:35", "17:45", "18:35", "18:50", "19:50", "03:15", "17:25", "23:55", "23:57", "23:59", "05:01", "10:30", "11:15", "13:00", "15:01", "20:31", "05:30", "11:30", "11:50", "15:30", "22:20", "08:15", "08:45", "10:10", "11:35", "12:55", "19:20", "21:25", "23:40", "04:40", "05:15", "05:20", "05:45", "06:00", "06:15", "07:45", "08:00", "08:25", "08:40", "23:50", "11:00", "11:20", "12:45", "14:45", "03:30", "03:35", "04:50", "11:45", "14:30", "17:15", "22:40", "18:30", "18:45", "19:15", "19:40", "19:45", "20:15", "22:35", "22:05", "09:20", "10:45", "04:15", "05:50", "18:20", "19:24", "21:20", "23:20", "06:45", "09:15", "13:15", "14:15", "07:15", "22:45", "20:35", "04:45", "05:35", "06:10", "06:20", "23:10", "13:45", "23:45", "22:25", "22:50", "23:05", "22:55", "09:45", "17:30", "21:40", "15:10", "03:40", "08:35", "23:15", "23:35", "09:40", "10:35", "11:05", "03:45", "03:50", "04:10", "21:02", "21:50", "00:45", "01:15", "00:30", "01:00", "01:30", "02:00", "00:15", "20:20", "08:50", "02:45", "16:35", "02:15", "01:25", "01:40", "01:45", "06:55", "00:22", "01:46", "02:07", "19:35", "20:10", "05:40", "09:05", "10:20", "19:10", "21:55", "06:50", "12:10", "16:10", "08:20", "15:15", "19:25", "14:40", "17:10", "17:20", "12:20", "12:25", "14:20", "15:40", "15:55", "17:40", "17:50", "12:40", "15:50", "13:10", "14:10", "14:35", "14:55", "15:05", "15:20", "16:50", "23:25", "16:40", "18:15", "14:25", "00:10", "23:38", "22:31", "18:40", "21:29", "21:31", "22:01", "15:22", "16:25", "16:01", "20:01", "21:05", "20:04", "17:29", "14:18", "13:05", "18:10", "23:44", "15:35", "18:06", "19:01", "17:55", "17:26", "20:25", "18:05", "13:26", "16:05", "14:05", "14:56", "13:35", "01:20", "14:29", "14:32", "17:59", "19:43", "17:05", "16:18", "17:18", "18:25", "20:29", "21:10", "19:55", "18:12", "21:35", "20:16", "23:21", "19:31", "20:36", "17:47", "22:02", "18:18", "16:06", "16:31", "17:04", "18:02", "17:01", "17:58", "18:04", "16:16", "17:31", "19:39", "20:33", "15:32", "17:02", "17:32", "23:46", "16:27", "16:02", "17:51", "19:02", "18:32", "19:03", "19:06", "19:58", "20:07", "20:32", "20:02", "15:31", "16:32", "17:28", "18:31", "19:59", "22:23", "23:49", "18:01", "16:47", "22:29", "23:58", "19:47", "20:09", "22:16", "15:46", "23:03", "19:16", "19:29", "22:14", "21:28", "04:53", "04:55", "05:10"])
    Reaching_time=slt.selectbox("Reaching Time:", ["18:22", "20:20", "21:25", "01:00", "23:45", "00:45", "01:25", "04:30", "03:45", "06:10", "06:55", "07:35", "06:30", "09:40", "09:00", "07:30", "05:45", "06:45", "10:14", "12:15", "12:30", "13:06", "14:14", "14:30", "14:01", "15:55", "15:10", "16:30", "16:00", "16:20", "18:19", "18:40", "20:00", "20:15", "19:50", "20:30", "21:05", "23:59", "01:30", "02:45", "01:29", "02:35", "15:20", "15:50", "16:45", "17:05", "18:30", "22:05", "03:15", "04:20", "05:15", "06:40", "06:35", "07:10", "06:13", "21:45", "06:00", "05:30", "06:15", "10:15", "11:15", "11:05", "11:40", "12:45", "13:25", "13:10", "14:25", "15:15", "15:08", "19:10", "18:55", "19:25", "20:45", "21:30", "22:20", "22:15", "22:00", "00:40", "03:00", "02:10", "02:30", "10:45", "12:10", "13:11", "16:05", "18:35", "19:15", "20:16", "21:35", "22:30", "23:00", "23:05", "11:16", "13:00", "13:30", "14:45", "14:55", "17:00", "18:00", "19:45", "22:40", "02:05", "04:25", "04:00", "16:10", "17:21", "21:00", "21:10", "20:50", "22:45", "23:55", "01:55", "01:01", "01:50", "02:50", "03:55", "02:55", "07:00", "12:35", "17:10", "17:20", "18:15", "18:50", "18:25", "19:00", "20:10", "00:05", "02:20", "04:05", "06:38", "03:30", "07:40", "09:30", "09:45", "08:20", "11:00", "11:30", "10:40", "10:20", "11:20", "12:40", "13:45", "07:45", "08:25", "08:55", "10:25", "10:50", "13:55", "15:45", "15:25", "17:45", "18:05", "06:50", "07:55", "11:10", "12:00", "19:30", "00:15", "04:45", "05:00", "05:40", "14:40", "04:15", "04:40", "04:50", "10:35", "12:05", "13:05", "14:05", "14:50", "16:15", "17:15", "16:50", "07:20", "08:40", "11:55", "14:15", "15:30", "23:30", "23:50", "02:00", "03:25", "17:35", "05:06", "05:46", "04:36", "05:36", "05:20", "04:55", "05:27", "04:34", "06:08", "05:55", "06:25", "10:32", "12:55", "13:40", "15:00", "15:40", "17:30", "17:40", "20:25", "10:10", "11:18", "10:30", "02:15", "23:35", "00:20", "10:00", "09:50", "11:45", "01:40", "13:15", "15:02", "18:10", "19:20", "05:50", "15:09", "16:39", "02:44", "03:19", "03:09", "03:42", "03:58", "03:49", "04:42", "06:20", "14:00", "02:40", "03:50", "04:10", "04:35", "07:15", "08:50", "18:20", "03:10", "03:40", "12:20", "13:35", "08:05", "08:15", "08:30", "05:10", "05:35", "07:12", "06:27", "05:26", "07:50", "08:00", "08:10", "23:20", "18:45", "23:15", "00:30", "00:03", "03:02", "03:20", "04:16", "03:05", "05:25", "04:43", "05:43", "06:58", "09:15", "08:35", "03:35", "09:54", "10:54", "11:54", "16:09", "17:55", "06:05", "07:09", "07:05", "07:34", "08:34", "11:34", "12:04", "12:49", "13:34", "14:34", "17:34", "18:34", "21:24", "22:04", "01:34", "02:04", "03:04", "15:05", "17:46", "11:35", "21:15", "16:40", "19:05", "05:05", "14:07", "01:10", "02:25", "22:50", "04:06", "15:35", "17:50", "00:50", "12:50", "16:55", "20:05", "21:55", "20:40", "21:20", "22:10", "01:20", "19:40", "19:55", "21:40", "22:35", "00:10", "00:55", "00:35", "01:45", "20:55", "23:40", "23:10", "04:29", "07:25", "00:00", "20:35", "06:39", "06:22", "17:25", "22:25", "01:15", "18:48", "22:55", "04:54", "23:31", "21:56", "19:52", "17:01", "23:25", "00:25", "23:42", "01:54", "16:35", "09:05", "20:48", "04:57", "05:12", "06:52", "05:48", "21:21", "22:26", "23:41", "00:21", "01:05", "21:38", "08:45", "21:50", "05:41", "07:27", "08:58", "05:16", "05:52", "04:46", "21:16", "22:31", "01:03", "22:01", "23:01", "05:33", "18:11", "19:31", "19:49", "20:29", "20:57", "08:01", "04:31", "06:02", "22:34", "21:36", "03:51", "21:32", "02:13", "01:35", "04:13", "08:56", "05:01", "20:44", "22:09", "21:53", "03:32", "03:59", "02:41", "02:22", "01:58", "02:34", "04:37", "03:01", "03:07", "06:46", "21:17", "23:02", "01:02", "02:43", "02:14", "22:21", "23:58", "06:29", "01:31", "05:44", "02:08", "06:01", "23:23", "01:37", "02:47", "03:31", "05:58", "01:21", "23:21", "00:51", "05:14"])
    Seat_available=slt.selectbox("Seat Available:", ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"])
#Kerala
    if S == "Kerala":
        K = slt.selectbox("List of routes", lists_K)
        
        # Fetch data based on the user's selection
        data = fetch_bus_data(K, select_fare, bus_type, Rating, Departing_time, Reaching_time, Seat_available)
        
        if data:
            df = pd.DataFrame(data, columns=["ID", "Bus_name", "Bus_type", "Departing_time", "Reaching_time", "Duration", "Price", "Star_Rating", "Seat_availabe", "Route_links", "Route_names"])
            slt.write(df)
        else:
            slt.write("No data found.")
#Andra
    if S == "Andhra Pradesh":
        A = slt.selectbox("List of routes", lists_A)
        
        # Fetch data based on the user's selection
        data = fetch_bus_data(A, select_fare, bus_type, Rating, Departing_time, Reaching_time, Seat_available)
        
        if data:
            df = pd.DataFrame(data, columns=["ID", "Bus_name", "Bus_type", "Departing_time", "Reaching_time", "Duration", "Price", "Star_Rating", "Seat_availabe", "Route_links", "Route_names"])
            slt.write(df)
        else:
            slt.write("No data found.")        
#Telugna
    if S == "Telugana":
        T = slt.selectbox("List of routes", lists_T)
        
        # Fetch data based on the user's selection
        data = fetch_bus_data(T, select_fare, bus_type, Rating, Departing_time, Reaching_time, Seat_available)
        
        if data:
            df = pd.DataFrame(data, columns=["ID", "Bus_name", "Bus_type", "Departing_time", "Reaching_time", "Duration", "Price", "Star_Rating", "Seat_availabe", "Route_links", "Route_names"])
            slt.write(df)
        else:
            slt.write("No data found.")
#Goa
    if S == "Goa":
        G = slt.selectbox("List of routes", lists_G)
        
        # Fetch data based on the user's selection
        data = fetch_bus_data(G, select_fare, bus_type, Rating, Departing_time, Reaching_time, Seat_available)
        
        if data:
            df = pd.DataFrame(data, columns=["ID", "Bus_name", "Bus_type", "Departing_time", "Reaching_time", "Duration", "Price", "Star_Rating", "Seat_availabe", "Route_links", "Route_names"])
            slt.write(df)
        else:
            slt.write("No data found.")
#Rajastan
    if S == "Rajastan":
        R = slt.selectbox("List of routes", lists_R)
        
        # Fetch data based on the user's selection
        data = fetch_bus_data(R, select_fare, bus_type, Rating,Departing_time, Reaching_time, Seat_available)
        
        if data:
            df = pd.DataFrame(data, columns=["ID", "Bus_name", "Bus_type", "Departing_time", "Reaching_time", "Duration", "Price", "Star_Rating", "Seat_availabe", "Route_links", "Route_names"])
            slt.write(df)
        else:
            slt.write("No data found.")
#South Bengal
    if S == "South Bengal":
        SB = slt.selectbox("List of routes", lists_SB)
        
        # Fetch data based on the user's selection
        data = fetch_bus_data(SB, select_fare, bus_type, Rating,Departing_time, Reaching_time, Seat_available)
        
        if data:
            df = pd.DataFrame(data, columns=["ID", "Bus_name", "Bus_type", "Departing_time", "Reaching_time", "Duration", "Price", "Star_Rating", "Seat_availabe", "Route_links", "Route_names"])
            slt.write(df)
        else:
            slt.write("No data found.")
#Haryana
    if S == "Haryana":
        H = slt.selectbox("List of routes", lists_H)
        
        # Fetch data based on the user's selection
        data = fetch_bus_data(H, select_fare, bus_type, Rating, Departing_time, Reaching_time, Seat_available)
        
        if data:
            df = pd.DataFrame(data, columns=["ID", "Bus_name", "Bus_type", "Departing_time", "Reaching_time", "Duration", "Price", "Star_Rating", "Seat_availabe", "Route_links", "Route_names"])
            slt.write(df)
        else:
            slt.write("No data found.")
#Assam
    if S == "Assam":
        AS = slt.selectbox("List of routes", lists_AS)
        
        # Fetch data based on the user's selection
        data = fetch_bus_data(AS, select_fare, bus_type, Rating, Departing_time, Reaching_time, Seat_available)
        
        if data:
            df = pd.DataFrame(data, columns=["ID", "Bus_name", "Bus_type", "Departing_time", "Reaching_time", "Duration", "Price", "Star_Rating", "Seat_availabe", "Route_links", "Route_names"])
            slt.write(df)
        else:
            slt.write("No data found.")
#Uttra Pradesh            
    if S == "Uttra Pradesh":
        UP = slt.selectbox("List of routes", lists_UP)
        
        # Fetch data based on the user's selection
        data = fetch_bus_data(UP, select_fare, bus_type, Rating, Departing_time, Reaching_time, Seat_available)
        
        if data:
            df = pd.DataFrame(data, columns=["ID", "Bus_name", "Bus_type", "Departing_time", "Reaching_time", "Duration", "Price", "Star_Rating", "Seat_availabe", "Route_links", "Route_names"])
            slt.write(df)
        else:
            slt.write("No data found.")
#West Bengal
    if S == "West Bengal":
        WB = slt.selectbox("List of routes", lists_WB)
        
        # Fetch data based on the user's selection
        data = fetch_bus_data(WB, select_fare, bus_type,Rating, Departing_time, Reaching_time, Seat_available)
        
        if data:
            df = pd.DataFrame(data, columns=["ID", "Bus_name", "Bus_type", "Departing_time", "Reaching_time", "Duration", "Price", "Star_Rating", "Seat_availabe", "Route_links", "Route_names"])
            slt.write(df)
        else:
            slt.write("No data found.")