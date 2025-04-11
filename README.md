to export requirements.txt with poetry

https://github.com/python-poetry/poetry-plugin-export



# Web Scrapping Alert

## Getting Started

This guide will walk you through the steps to set up and replicate this project on your local machine and deploy it on AWS with Docker. You can choose to manage the project dependencies using either [Poetry](https://python-poetry.org/) or [pip](https://pypi.org/project/pip/).

### Prerequisites

* **Python 3.6:** Make sure you have a compatible Python 3 version installed on your system. You can check your Python version by running `python --version` or `python3 --version` in your terminal.

## Libraries Used and Explanation

1. **requests**: Used to make HTTP requests and fetch HTML from web pages.
2. **BeautifulSoup (bs4)**: Used to parse and extract specific information from the page's HTML, such as the product price.
3. **time**: A library for scheduling tasks, allowing price checks at regular intervals.
4. **pandas**: Makes data manipulation easier, allowing saving and loading of price history in CSV files.
5. **sqlite3**: A lightweight SQLite database used to store and organize price data over time.
6. **python-telegram-bot**: A library for sending messages to Telegram, notifying the user when the price hits a specific value.
7. **python-dotenv**: Loads environment variables from a `.env` file, where sensitive information like the Telegram token and chat ID are stored.

### Option 1: Setting up with Poetry (Recommended)

[Poetry](https://python-poetry.org/) is a tool for dependency management and packaging in Python. It provides a consistent and streamlined way to manage your project's dependencies.

1.  **Install Poetry:** If you don't have Poetry installed, you can install it by running the following command in your terminal:

    ```bash
    pip install poetry
    ```

    or using pipx

    ```bash
    pipx install poetry
    ```

    Make sure to add Poetry to your system's PATH environment variable if necessary. You can verify the installation by running `poetry --version`.

3.  **Clone the Repository:** Clone your project repository from GitHub to your local machine:

    ```bash
    git clone <your_repository_url>
    cd <your_project_directory>
    ```

    Replace `<your_repository_url>` with the actual URL of your GitHub repository and `<your_project_directory>` with the name of the cloned directory.

4.  **Install Dependencies:** Navigate to the project directory (where the `pyproject.toml` file is located) and run the following command to install all the project dependencies:

    ```bash
    poetry install
    ```

    Poetry will read the `pyproject.toml` and `poetry.lock` files to install the exact versions of the dependencies specified.

5.  **Run the Project:** Now that the dependencies are installed and the virtual environment is active, you can run your project according to its instructions (e.g., `python main.py`, `streamlit run app.py`, etc.). Refer to the specific instructions in your README or project documentation.

### Option 2: Setting up with pip

[pip](https://pypi.org/project/pip/) is the package installer for Python. While it requires manual management of virtual environments, it's a widely used tool.

1.  **Clone the Repository:** Clone your project repository from GitHub to your local machine:

    ```bash
    git clone <your_repository_url>
    cd <your_project_directory>
    ```

    Replace `<your_repository_url>` with the actual URL of your GitHub repository and `<your_project_directory>` with the name of the cloned directory.

2.  **Create a Virtual Environment (Recommended):** It's highly recommended to create a virtual environment to isolate your project's dependencies. You can do this using Python's built-in `venv` module:

    ```bash
    python -m venv venv
    ```

    or

    ```bash
    python3 -m venv venv
    ```

    This will create a directory named `venv` in your project directory.

3.  **Activate the Virtual Environment:** Activate the virtual environment based on your operating system:

    * **Linux/macOS:**

        ```bash
        source venv/bin/activate
        ```

    * **Windows (Command Prompt):**

        ```bash
        venv\Scripts\activate
        ```

    * **Windows (PowerShell):**

        ```powershell
        .\venv\Scripts\Activate.ps1
        ```

    Once activated, your terminal prompt will likely be prefixed with `(venv)`.

4.  **Install Dependencies:** Navigate to the project directory (where the `requirements.txt` file is located, if you have one). If you have a `requirements.txt` file, install the dependencies using pip:

    ```bash
    pip install -r requirements.txt
    ```

    If you don't have a `requirements.txt` file, you'll need to manually install the required packages using `pip install <package_name>`. Make sure to list all the necessary dependencies in your README if you don't provide a `requirements.txt` file.

5.  **Run the Project:** With the dependencies installed and the virtual environment active, you can now run your project according to its instructions (e.g., `python main.py`, `streamlit run app.py`, etc.). Refer to the specific instructions in your README or project documentation.

## Contributing

[Explain how others can contribute to your project. This might include guidelines for submitting pull requests, reporting issues, etc.]

## License

[Specify the license under which your project is distributed. If you included a license badge at the top, make sure the `LICENSE` file exists in your repository.]

## Acknowledgements

[Optional: Mention any libraries, frameworks, or individuals that helped in the development of your project.]
