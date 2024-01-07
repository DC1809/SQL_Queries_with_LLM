# Aura Merchandise Database Q&A

##Description
This project is a Streamlit-based Q&A application for interacting with the Aura Merchandise database. It uses LangChain for generating natural language queries and executing them on a MySQL database.

##Prerequisites
- Python 3.11 or newer.
- MySQL Workbench.
- A Google API key for LangChain.

## Database Setup
Open MySQL Workbench and connect to your MySQL server.
Copy the sql code inside Aura Merchendise DB in the workbench and it will create the database with all the couloms.

##Running the Application

-Set Up Environment Variables: Set your Google API key in the environment variables or directly in the script.
-Start the Streamlit App:
-Interact with the App: Open your browser to the provided URL (usually http://localhost:8501). Input your queries in the Streamlit interface and receive answers.

##Usage Example
- Navigate to the Streamlit app.
- In the "Question:" input field, type a query like "How many t-shirts do we have left for Nike in XS size and white color?"
- Press enter or click the submit button to get the answer.

