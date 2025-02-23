Project Title: Car Price Estimation with Decision Tree

Description:
This project uses a Decision Tree model to estimate the price of a car based on the user's input. The workflow is as follows:

1. User Input: The user provides the brand, model, year of manufacture, and mileage of the car.


2. Web Scraping: Using BeautifulSoup 4, the project scrapes relevant car price data from the TrueCar website based on the provided brand and model.


3. Database Storage: The scraped data is stored in a MariaDB database, ensuring efficient and structured storage for easy retrieval.


4. Decision Tree Model: A Decision Tree model is trained using the data stored in the database. The model learns the relationships between car features, such as brand, model, year, mileage, and their corresponding prices.


5. Price Estimation: After training, the model is used to predict the price of a car based on the user's input data.



This project combines web scraping, data storage with MariaDB, and machine learning to create a real-world application for car price estimation.

Technologies Used:

Python

BeautifulSoup 4

MariaDB

scikit-learn (for Decision Tree model)

Requests
