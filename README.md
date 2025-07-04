# COVID-19-Data-Analysis
📝 Objective: To analyze a real-world COVID-19 dataset using the pandas library and extract valuable insights such as total cases, deaths, recoveries, and trends over time for different countries.

🛠️ Tools and Libraries: Python 3

Pandas

Matplotlib

(Optional) NumPy

📂 Dataset Source: The dataset used is a CSV file named covid_19_data.csv, which contains columns like:

ObservationDate

Province/State

Country/Region

Last Update

Confirmed

Deaths

Recovered

📊 Key Steps: Data Loading: The dataset was loaded using pandas.read_csv().

Data Cleaning:

Renamed columns for clarity.

Converted date strings into datetime format.

Filled missing values in State, Confirmed, Deaths, and Recovered.

Data Analysis:

Total confirmed cases by country.

Sorted top 10 countries based on confirmed cases.

Grouped data by date and country for deeper analysis.

Visualization:

Bar graph of the top 5 countries by confirmed cases.

Line chart showing trend of confirmed cases in India over time.

📈 Observations: The countries with the highest number of confirmed cases include the USA, India, Brazil, and Russia.

A consistent rise in COVID-19 cases was observed over time in India.

The dataset allowed for trend tracking and insights into outbreak patterns.

📌 Conclusion: Using pandas, we efficiently cleaned and analyzed COVID-19 data to discover meaningful trends and patterns. The project highlights how data science tools can be used for real-world health data analysis and decision-making.


