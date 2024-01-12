## Infinite_FE_Framework

### Environment Setup

1. Global Dependencies
  * [Install Python](https://www.python.org/downloads/)
  * Or Install Python with [Homebrew](http://brew.sh/)
  ```
  $ brew install python
  ```
  * Install [pip](https://pip.pypa.io/en/stable/installing/) for package installation
  * Install [Allure Report](https://allurereport.org/docs/gettingstarted-installation/) for report view

2. Project
  * The recommended way to run your tests would be in [virtualenv](https://virtualenv.readthedocs.org/en/latest/). It will isolate the build from other setups you may have running and ensure that the tests run with the specified versions of the modules specified in the requirements.txt file.
  ```$ pip install virtualenv```
  * Create a virtual environment in your project folder the environment name is arbitrary.
  ```$ virtualenv venv```
  * Activate the environment:
  ```$ source venv/bin/activate```
  * Install the required packages:
  ```$ pip install -r requirements.txt```

### Running Tests: 

*  Tests in Parallel: To run tests in parallel against a single browser, run :
    ```
      pytest -n=3 tests/ --alluredir allure_result
    ```

### View Reporst

*  Reports can be viewd by Allure Report
    ```
      allure serve allure_result
    ```