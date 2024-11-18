-----Infosys-Chatbot-A-Streamlit-Based-Interactive-Q-A-Application-----
This code provides an Infosys chatbot application using Streamlit, a Python framework  for building web applications

---

# Infosys Chatbot

A **Streamlit-based Interactive Q&A Application** designed to provide instant responses to queries about Infosys. This project uses a simple keyword-based approach to simulate a chatbot experience.

1. FEATURES

- **Interactive User Interface**: Built with Streamlit for seamless interactions.
- **Knowledge Base**: Predefined set of Q&A covering Infosys' history, achievements, and services.
- **Enhanced Response Matching**: 
  - Case-insensitive input matching.
  - Fallback and default responses for unmatched queries.
- **Session Persistence**: Maintains a conversation history within the session for continuous interactions.

2. TECH STACK

- **Python**: Backend programming.
- **Streamlit**: Frontend framework for building web applications.

---

3. GETTING STARTED

3.1. PREREQUSITION 

Ensure you have the following installed:
- Python (>=3.7)
- pip (Python package manager)

3.2. INSTALLATION

1. Clone the repository:
   ```bash
   git clone https://github.com/<your-username>/infosys-chatbot.git
   cd infosys-chatbot
   ```

2. Install required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:
   ```bash
   streamlit run chatbot.py
   ```

---

3.3. USAGE

1. Open the chatbot application in your browser.
2. Enter your query about Infosys in the input box.
3. View responses and a history of interactions.

---

3.4. CODE OVERVIEW

### Main Components

1. Knowledge Base:
   A dictionary (`infosys_data`) containing predefined questions and answers.

2. Response Matching:
   The `get_infosys_response()` function standardizes user inputs and matches them with the knowledge base.

3. Session Handling:
   Maintains chat history using Streamlit's `st.session_state`.

4. Frontend:
   - Title and instructions.
   - Input box for queries.
   - Display of chat history and responses.

---

4. CONTRIBUTING

We welcome contributions! Please fork this repository, make your changes, and submit a pull request. Ensure your code adheres to our style guidelines.

---

5. LICENSE

This project is licensed under the MIT License - see the `LICENSE` file for details.

---

6. CONTACT

For questions or support, please contact:
- [VIGNESH T](mailto:vignesht20@dsce.ac.in)

---

Let me know if you need further customizations!
