
# : Simplifying Data for Everyone with AI-Powered Natural Language Queries and Seamless Data Visualization.

Welcome to Neural Query! This project aims to simplify data access and manipulation in SQL databases through natural language commands, educational examples, and powerful AI integration.

![image](https://github.com/user-attachments/assets/27029210-e37c-41a5-aaea-2e706c9ba611)


## Features

### 1. Natural Language SQL Query Generation
- **Query Simplification:** Generate SQL queries by simply typing your request in plain language.
- **Output Understanding:** Receive explanations for each query, breaking down the syntax and logic used.

### 2. SQL Formatter
- **Code Organization:** Format and clean up your SQL code for better readability and maintenance.

### 3. Query Explainer
- **Detailed Breakdown:** Analyze complex SQL queries with explanations for each component, making them easier to understand.

### 4. Data Analysis & Visualization
- **Visual Insights:** Generate charts and visualizations directly from your queries to better understand your data.

## Built With

- **Languages:** Python
- **Frameworks:** Streamlit
- **Cloud Services:** Google Cloud Platform (GCP)
- **Databases:** SQLite
- **APIs:** Gemini 1.5 Pro API
- **Data Visualization:** Plotly Express
- **AI & NLP:** Google’s Generative AI tools

## Project Architecture

- **Frontend:** Built with Streamlit for a user-friendly interface.
- **Backend:** Powered by Python and integrated with the Gemini 1.5 Pro API for AI capabilities.
- **Database:** Managed with SQLite, ensuring lightweight and efficient data management.

## Setup Instructions

1. **Clone the Repository:**
    ```bash
    https://github.com/vikash-kumar-swiggy/Swiggy-hackathon.git
    ```
    ```bash
    cd Swiggy-hackathon
    ```

2. **Install the required libraries:**
    ```bash
    pip install -r requirements.txt
    ```

3. **Set Up SQLite Database:**
    - No additional setup is required for SQLite; it is lightweight and runs locally by default.

4. **Environment Variables:**
    ```bash
    export GOOGLE_API_KEY=your_google_api_key
    ```

5. **Run the Application:**
    ```bash
    streamlit run app.py
    ```
    - This will launch a web app in your default browser, usually at http://localhost:8501.
  
6. ![image](https://github.com/user-attachments/assets/64d57451-4be9-42cc-ba64-876d3d478c72)


## Testing Instructions

1. **Access the Application:** Follow the setup instructions to run the application locally.
2. **Database Connection:** Ensure that SQLite is correctly configured and accessible.
3. **Run Queries:** Input natural language commands and observe the generated SQL queries and their explanations.
4. **Test Features:** Use the SQL Formatter and Query Explainer to test formatting and query explanation functionalities.

## Challenges and Learnings

1. **Integration:** Successfully integrated SQLite with the AI-powered GenQuery to manage data efficiently.
2. **User Experience:** Focused on making the tool beginner-friendly while maintaining powerful features for advanced users.

## Future Enhancements

1. **User Feedback Integration:** Gather user feedback to further improve the tool.
2. **Expanded Features:** Plan to add more data visualization options and AI-driven insights.
