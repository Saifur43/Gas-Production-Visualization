Here's a `README.md` template for your gas field production data analysis Django project. It includes sections that outline the project's purpose, setup instructions, usage, and more.

---

# Gas Field Production Data Analysis Dashboard

This project is a Django web application that visualizes production data for gas fields. It provides an interactive dashboard where users can filter by gas fields, wells, date ranges, and data attributes, and it offers various customization options, such as enabling logarithmic scales. The dashboard also supports exporting the analysis as a PDF.

## Features

- Interactive filtering of gas field production data
- Visualization of production rates and cumulative values for selected wells
- Date range selection and X/Y-axis parameter options
- Logarithmic scale option for the Y-axis
- PDF export functionality with selected filter options

## Prerequisites

- **Python**: Version 3.7 or higher
- **Django**: Version 3.2 or higher
- **Chart.js**: Used for generating the interactive charts
- **Bootstrap**: Used for styling the dashboard

## Installation

1. **Clone the repository**:

    ```bash
    git clone https://github.com/yourusername/gas-field-dashboard.git
    cd gas-field-dashboard
    ```

2. **Set up a virtual environment**:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. **Install dependencies**:

    ```bash
    pip install -r requirements.txt
    ```

4. **Apply migrations**:

    ```bash
    python manage.py migrate
    ```

5. **Create a superuser** (optional, for accessing Django admin):

    ```bash
    python manage.py createsuperuser
    ```

6. **Run the development server**:

    ```bash
    python manage.py runserver
    ```

7. **Access the application**:
   - Open a browser and navigate to `http://127.0.0.1:8000` to access the dashboard.

## Usage

1. **Navigate to the Dashboard**:
   - The main dashboard displays a sidebar with filter options for gas fields, wells, date range, and X/Y-axis parameters.

2. **Filter Production Data**:
   - Select a gas field, then choose specific wells and parameters to analyze.
   - Customize the date range and enable/disable the logarithmic scale as needed.

3. **Export as PDF**:
   - Click the **Export as PDF** button at the top-right of the dashboard to save the current chart view, including selected options, as a PDF.

## Project Structure

- `gas_field_dashboard/`: Main Django app for the project.
  - `models.py`: Contains models for `GasField`, `Well`, and `ProductionData`.
  - `views.py`: Defines views for rendering the dashboard, fetching well data, and exporting PDFs.
  - `templates/`: Contains HTML templates for the dashboard and export features.
  - `static/`: Static files for styling (CSS) and JavaScript.

## API Endpoints

The application provides several API endpoints for retrieving production data and well details:

- `/api/well-data/`: Retrieves production data for specified wells and date ranges.
- `/api/field-wells/`: Fetches well names for a selected gas field.

## PDF Export

The dashboard includes a **PDF export** feature, allowing users to download the currently displayed chart with selected options.

## Customization

- **Styles**: Customize styles in `static/css/styles.css` or adjust Bootstrap classes in the templates.
- **Charts**: Chart.js options can be modified in the JavaScript included in the dashboard template.

## Contributing

1. Fork the repository
2. Create a new branch for your feature or bug fix:
   ```bash
   git checkout -b feature-name
   ```
3. Commit changes:
   ```bash
   git commit -m "Add feature name"
   ```
4. Push to your branch and create a pull request.

## License

This project is licensed under the MIT License.

## Acknowledgments

- Chart.js for charting functionality
- Bootstrap for frontend styling

---

Feel free to expand on any sections or adjust details specific to your setup or requirements!