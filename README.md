# Red-Bus-Routes

**Redbus Data Scraping with Selenium & Dynamic Filtering using Streamlit**

**Domain**: Bus Transportation

**Ojective**:
The Redbus Data Scraping and Filtering with streamlit Application aims to enhance the experience of travelers and bus service providers by scraping bus route data from the popular transportation platform.

_**Overview**:_

**Data Scraping with Selenium:**

**Purpose:** Extract live bus data such as routes, timings, prices, and seat availability from Redbus.

**Approach:**
Automating browser interactions to navigate through Redbus pages.
Capturing relevant data fields dynamically rendered using JavaScript (e.g., bus schedules, ticket prices, reviews).
Managing challenges like captchas, dynamic elements, and page delays with Selenium-specific techniques (e.g., WebDriverWait and XPath).

**Dynamic Filtering with Streamlit:**

**Purpose:** Enable users to explore and analyze the scraped data interactively.

**Features:**
Real-time filters for routes, pricing ranges, departure/arrival times, and bus operators.
Visualization options like tables, bar charts, and line plots for better insights.
Clean, user-friendly interface with instant updates on filtered results.

**Integration Workflow:**

Scraped data from Selenium is stored in structured formats (e.g., Pandas DataFrame).
The data is then fed into a Streamlit application for interactive filtering and visualization.
Users can filter results to find the most suitable travel options according to their preferences.

**Project Highlights:**

**Technology Stack:** Combines web scraping, data manipulation, and web app frameworks for an end-to-end solution.
Automation: Handles dynamic and JavaScript-rendered web content seamlessly.
**User-Centric Interface:** Provides a practical tool for users to analyze and customize their travel plans effectively.

**Applications:**
Real-time travel planning and price comparison.
Insights into bus availability and operator trends.

**Programm Languages and packages used to fetching data and storing data in database and deleveping application using streamlit**

**Selenium**: Selenium is a library used for automating web browser. It is commonly used for web scraping, which involves extracting data from websites.

**Pandas**: Use the powerful Pandas library to transform the dataset from CSV format into a structured dataframe. Pandas helps data manipulation, cleaning and preprocessing, ensuring that data was ready for analysis.

**MySQL**: With help of sql to establish a connection to a SQL database, enabling seamless intergration of the transformed dataset and the data was efficiently inserted into relevent tables for storage and retrieval.

**Streamlit**: Developed an interactive web application using Streamlit, a user-friendly framework for data visualization and analysis.

**Skill-take**:
Selenium, Python, Pandas, MySQL, Streamlit.

**Developed-by**: Karthik Anbazhagan

**Icons like Home and States and Routes are created:**
![image](https://github.com/user-attachments/assets/4519e037-304f-4ac5-b535-044e8d430ccf)

**About the project overview using streamlit code are created:**
![image](https://github.com/user-attachments/assets/2c899020-410d-4a0c-b207-9f5ee6f6277d)

**Once click on Sates and Routes Icons able to acces list of state and price sorting options**
![image](https://github.com/user-attachments/assets/81083b5c-1f57-45a2-a7ea-c0947c65c979)

**List of States are created in dropdown options**
![image](https://github.com/user-attachments/assets/b9ea50f6-9772-41c7-aa5d-94a42ccc9a9c)

**Price sorting options depanding on the condition list of routes are suggested**
![image](https://github.com/user-attachments/assets/6a2ebac7-6789-4519-a483-d9dff67c0d6a)

**Final Output:**
![image](https://github.com/user-attachments/assets/e9fc39c5-da61-49c6-bbad-d3116c8edccc)




