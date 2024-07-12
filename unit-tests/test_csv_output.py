import csv
import os
from io import StringIO
from utils import csv_output


def test_csv_output():
    result = [
        ["TestCase ID", "Master Option For Option1", "Master Option For Option2", "Client Option For Option1",
         "Client Option For Option2", "Valid TC", "Expected Option1", "Expected Option2"],
        [1, "NA", "TRUE", "TRUE", "NA", "YES", "TRUE", "TRUE"],
        [2, "FALSE", "NA", "NA", "TRUE", "YES", "FALSE", "TRUE"],
        [3, "NA", "NA", "FALSE", "FALSE", "NO", "NA", "NA"]
    ]
    csv_output(result, "test_output.csv")
    assert os.path.exists("test_output.csv"), "File 'output.csv' was not created"

    with open("test_output.csv", 'r', newline='') as f:
        csv_content = f.read()

    output = StringIO()
    csv_writer = csv.writer(output, delimiter=',')
    csv_writer.writerows(result)
    expected_csv_content = output.getvalue()
    assert csv_content == expected_csv_content, f"CSV content does not match. Expected:\n{expected_csv_content}\nBut got:\n{csv_content}"

    os.remove("test_output.csv")


def test_csv_output_empty_data():
    result = []
    csv_output(result, "test_empty_output.csv")
    assert os.path.exists("test_empty_output.csv"), "File 'test_empty_output.csv' was not created"
    with open("test_empty_output.csv", 'r', newline='') as file:
        csv_content = file.read()
    assert csv_content == "", "CSV content should be empty for empty data"

    os.remove("test_empty_output.csv")
