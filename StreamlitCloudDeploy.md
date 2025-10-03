# Streamlit Community Cloud Deployment Instructions

Deploying your Streamlit application to Streamlit Community Cloud is straightforward, especially if your code is hosted on GitHub.

## Prerequisites

1. **GitHub Repository:** Your Streamlit app code (including `app.py`, `requirements.txt`, etc.) must be in a public or private GitHub repository.
2. **Streamlit Community Cloud Account:** You need to have an account. You can sign up for free using your GitHub account at [share.streamlit.io](https://share.streamlit.io/).

## Deployment Steps

1. **Log in to Streamlit Community Cloud:**

    - Navigate to [share.streamlit.io](https://share.streamlit.io/) and log in.

2. **Create a New App:**

    - From your workspace, click the "**New app**" button.

3. **Configure Your App:**

    - **Repository:** Choose the GitHub repository where your project is located.
    - **Branch:** Select the branch you want to deploy (e.g., `main` or `master`).
    - **Main file path:** Ensure this is set to your main Python script, which is typically `app.py`.
    - **App URL (Optional):** You can customize the URL for your application.

4. **Deploy:**

    - Click the "**Deploy!**" button.

Streamlit will then build the environment by installing the dependencies from your `requirements.txt` file and run your application. You will be able to see the deployment progress and access your live application once it's finished.
