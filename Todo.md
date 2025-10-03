# To-Do List for Interactive Linear Regression App

## 1. Project Setup

-   [ ] Define project requirements based on HW1.
-   [ ] Set up project structure and version control with Git.
-   [ ] Create `requirements.txt` with necessary libraries (streamlit, scikit-learn, pandas, altair).

## 2. Streamlit UI Development

-   [ ] Create the main application file `app.py`.
-   [ ] Set up the page layout, title, and descriptive text.
-   [ ] Implement a sidebar for user controls.
-   [ ] Add sliders for `n` (number of points), `a` (coefficient), and `noise` (variance).

## 3. Core Logic Implementation

-   [ ] Write a function to generate synthetic data based on user inputs.
-   [ ] Use `scikit-learn`'s `LinearRegression` to train a model on the generated data.
-   [ ] Make predictions using the trained model.

## 4. Visualization & Evaluation

-   [ ] Use Altair to create an interactive chart showing:
    -   [ ] Scatter plot of the data points.
    -   [ ] The fitted regression line.
-   [ ] Display model evaluation metrics (MSE and R-squared).
-   [ ] Identify and display the top 5 outliers.

## 5. Deployment

-   [ ] Ensure the app runs correctly locally.
-   [ ] Push the final code to a GitHub repository.
-   [ ] Deploy the application to Streamlit Community Cloud.
-   [ ] Update `README.md` with the public app URL.
