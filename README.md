# Server-Client Config
<h3>
A Python program to simulate and test the configuration of a server by master and slave clients. It generates all possible combinations of Boolean server options and records the expected results in a CSV file.
</h3>

# Assumptions
<ul>
    <li>If slave client configures the server with same values already set by master client, no error 
message will be shown</li>
    <li>If slave client configures the server with default value, also does not contradict with master, no error 
message will be shown</li>
    <li>Server all options Default value = TRUE </li>
    <li>A test case is invalid if it does not follow the rules</li>
    <li>An indeed invalid test case, then all expected options' values are set to "NA"</li>
</ul>

## Documents
1. <a href="https://github.com/AbdallahSalah003/server-client-config/blob/main/code-structure-diagram.png">Code Structure Diagram</a>
2. <a href="https://github.com/AbdallahSalah003/server-client-config/blob/main/all-test-cases.pdf">Report With All Test Cases</a>
3. <a href="https://github.com/AbdallahSalah003/server-client-config/blob/main/unit-integration-testing.pdf">Report With Unit and Integration Test Cases</a>
4. <a href="https://github.com/AbdallahSalah003/server-client-config/blob/main/output.csv">Sample output: output.csv</a>
5. <a href="https://github.com/AbdallahSalah003/server-client-config/blob/main/README.md">README.md</a>

## Built With
[![python][python]][python-url] [![pytest][pytest]][pytest-url]

## How to Run
1. Clone the repository.
```
git clone https://github.com/AbdallahSalah003/server-client-config.git
```
2. install python3
```
sudo apt update
sudo apt install python3  
```
3. Navigate to the project dir and Run the following, replace [ option1, option2, ... , optionN ] with the server options
```
python3 main.py option1, option2, ..... , optionN
```
4. The program will run while the options are not valid or until press q to quit
4. To run unit and integration tests, install pytest first
```
pip install pytest
```
6. Run the following command to run all tests
```
python3 -m pytest
```



[python]: https://img.shields.io/badge/python-black?style=for-the-badge&logo=python
[python-url]: https://www.python.org/
[pytest]: https://img.shields.io/badge/pytest-darkblue?style=for-the-badge&logo=pytest
[pytest-url]: https://docs.pytest.org/en/8.2.x/