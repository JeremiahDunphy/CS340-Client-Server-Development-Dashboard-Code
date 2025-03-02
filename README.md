# Grazioso Salvare Dashboard

## Project Overview:
This project implements a web application dashboard for Grazioso Salvare, a rescue-animal training organization. The dashboard allows users to interact with and visualize data from the Austin Animal Center, filtering and displaying animal shelter outcomes relevant to the organization's needs. It is developed using the Dash framework, MongoDB as the database, and Python for the backend. This dashboard helps identify dogs suitable for search-and-rescue training.

## How to Use the Dashboard:
1. **Setting Up the Environment:**
   - Install Python 3.x and MongoDB.
   - Install required Python packages:
     ```bash
     pip install dash pandas pymongo plotly
     ```
2. **Importing the Dashboard Code:**
   - Clone the repository or use the provided `ProjectTwoDashboard.ipynb` file.
3. **Connecting to MongoDB:**
   - Ensure MongoDB is running and the data is loaded. The connection setup is done through the `AnimalShelter` class:
     ```python
     from crud import AnimalShelter
     username = "username"
     password = "password"
     host = "mongodb"
     port = 35180
     db_name = "AAC"
     collection_name = "animals"
     shelter = AnimalShelter(username, password, host, port, db_name, collection_name)
     ```
4. **Running the Dashboard:**
   - Run the Jupyter notebook:
     ```bash
     !jupyter notebook ProjectTwoDashboard.ipynb
     ```

## Key Features:
- **Interactive Data Table:** Displays animal shelter data with the ability to filter by rescue type and breed.
- **Geolocation Map:** Visualizes animal locations using a map with markers for each animal’s rescue location.
- **Graphical Analysis:** Uses Plotly to visualize animal data in a scatter plot for geospatial data.

---

## Responses to Questions:

### 1. How do you write programs that are maintainable, readable, and adaptable?
In my work on the CRUD Python module from Project One, I followed principles that enhance maintainability, readability, and adaptability:
- **Separation of Concerns:** The `AnimalShelter` class encapsulates all database interactions, making the code modular and reusable.
- **Clear Documentation:** The code is well-documented with docstrings to explain each method’s purpose and usage, which makes it easier for others to understand and maintain.
- **Error Handling:** Proper error handling ensures that the program can gracefully handle failures (e.g., connection issues), which improves its stability and adaptability.
- **Advantages:** This approach makes it easier to scale the project or integrate with other systems in the future. The CRUD module can also be reused in other projects that require similar MongoDB interactions.
  
### 2. How do you approach a problem as a computer scientist?
When working on the database and dashboard requirements for Grazioso Salvare, I took the following approach:
- **Understanding the Requirements:** First, I clarified the organization’s needs by discussing what data and functionalities were most important for the dashboard.
- **Designing a Scalable Solution:** I chose MongoDB because it offers flexibility and scalability for storing and retrieving large datasets.
- **Incremental Development:** I built the CRUD module to handle database interactions and connected it with the dashboard incrementally, testing each component as I went.
  
This approach differed from previous assignments in other courses because of the focus on integrating database queries with real-time data visualization in the dashboard. In future database projects, I will continue to prioritize modularity and scalability, using techniques like ORM (Object-Relational Mapping) or frameworks like Flask or Django to manage database interactions efficiently.

### 3. What do computer scientists do, and why does it matter?
Computer scientists design, implement, and optimize systems and software that solve problems. In this project, my work on the dashboard would help Grazioso Salvare by:
- **Streamlining Data Access:** By providing an intuitive interface to interact with data, the dashboard simplifies the process of finding relevant animals for training.
- **Supporting Decision-Making:** The visualizations and interactive features allow staff to make better-informed decisions regarding rescue operations.
- **Improving Efficiency:** By automating data retrieval and visualization, the organization can save time and focus more on mission-critical tasks, such as training and rescue operations.

In this way, computer science enables organizations like Grazioso Salvare to improve their operations and fulfill their mission more effectively.

---

## Conclusion:
This project provides an open-source solution for animal rescue organizations to manage and analyze animal shelter data. It combines the power of MongoDB, Python, and Dash to offer an interactive and dynamic dashboard that can be easily customized and expanded to fit the needs of similar organizations.