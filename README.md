# Data Visualization Project

This project is a data visualization tool built using Python and Streamlit. It allows users to explore and analyze data interactively. The application is designed to work with the datasets `hour_clean.csv` and `day_clean.csv`. The main script, `dashboard.py`, provides a simple and intuitive interface for users to engage with the visualizations.

## Features
- Interactive data visualization.
- User-friendly interface built with Streamlit.
- Ready for deployment using Streamlit sharing or local hosting.

## Requirements
Ensure you have the required dependencies installed. A `requirements.txt` file is provided to facilitate the installation of necessary packages.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/dzikrimaulana87/bike-rental-dashboard
   cd bike-rental-dashboard
   ```

2. Create a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Place the datasets `hour_clean.csv` and `day_clean.csv` in the project directory.

## Usage
1. Run the application locally:
   ```bash
   streamlit run dashboard.py
   ```

2. Access the application in your web browser at `http://localhost:8501`.

## Deployment
To deploy the application to Streamlit Cloud:
1. Push your repository to GitHub.
2. Log in to [Streamlit Cloud](https://streamlit.io/cloud) and link your repository.
3. Set the main file as `dashboard.py`.
4. Deploy the application.

## File Structure
- `dashboard.py`: Main application script.
- `hour_clean.csv`: Dataset containing hourly data.
- `day_clean.csv`: Dataset containing daily data.
- `requirements.txt`: List of dependencies.

## License
This project is licensed under the [MIT License](LICENSE).

---

For any issues or questions, feel free to open an issue in the repository or contact [me](https://www.linkedin.com/in/dzikrimaulana87/).
