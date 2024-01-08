import time
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from selenium import webdriver
from bs4 import BeautifulSoup
options = webdriver.ChromeOptions()
options.add_argument('--headless')  # Run Chrome in headless mode
options.add_argument("--no-sandbox")  # Bypass OS security model
options.add_argument("--disable-dev-shm-usage")  # Overcome limited resource problems
driver = webdriver.Chrome(options=options)

url = "https://www.bbc.com/weather/293397"
driver.get(url)
time.sleep(5)
html_content = driver.page_source

# Close the browser
driver.quit()

# Parse HTML with BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# Extract relevant data (modify as per your requirements)
dates = [date.text for date in soup.find_all("span", class_="wr-date__long")]
temperatures = [temp.text.replace('°', '') for temp in soup.find_all("span", class_="wr-value--temperature--c")]

# Organize the scraped data into a structured format (Pandas DataFrame)
weather_data = pd.DataFrame({'Date': dates, 'Temperature (°C)': temperatures})

# Clean and preprocess the data (type conversion, etc.)
weather_data['Temperature (°C)'] = weather_data['Temperature (°C)'].astype(float)

# Perform basic analysis
average_temperature = weather_data['Temperature (°C)'].mean()

sns.set_theme(style="whitegrid")
plt.figure(figsize=(10, 6))
sns.lineplot(x='Date', y='Temperature (°C)', data=weather_data, marker='o', color='blue')
plt.title('Temperature Trend in Tel Aviv')
plt.xlabel('Date')
plt.ylabel('Temperature (°C)')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig('temperature_trend.png')
plt.show()

# Document Your Findings (report summarizing your methodology, analysis, and insights)
print(f"Average Temperature: {average_temperature}°C")
print("Report: The line plot shows the temperature trend in Tel Aviv over the specified dates.")

# You can also export the DataFrame to CSV or Excel for further analysis
weather_data.to_csv('weather_data.csv', index=False)