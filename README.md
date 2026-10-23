# Urban Grocers — API Test Automation

API testing project developed as part of the TripleTen QA Engineering program. It uses Python, pytest, and Requests to validate the `name` field when creating a product kit.

## Project Objective

Check that the API accepts valid kit names and rejects values that do not meet the requirements.

Each test creates a user, obtains an authentication token, and uses that token to send a kit-creation request.

## Technologies

- Python
- pytest
- Requests
- HTTP and JSON
- Bearer authentication
- Git and GitHub

## Test Coverage

| Scenario | Expected HTTP status |
| --- | --- |
| Name with 1 character | 201 |
| Name with 511 characters | 201 |
| Empty name | 400 |
| Name with 512 characters | 400 |
| Name containing special characters | 201 |
| Name containing spaces | 201 |
| Name containing numeric characters as a string | 201 |
| Request without the `name` field | 400 |
| Numeric value instead of a string | 400 |

Positive tests also verify that the returned name matches the submitted value.

## My Contribution

I implemented test data preparation, reusable request functions, authentication-token retrieval, and positive and negative assertions.

I organized the project into separate modules for configuration, data, HTTP requests, and tests. I also compared expected and actual responses to identify validation discrepancies.

## Repository Structure

- `configuration.py`: Server URL and endpoint paths.
- `data.py`: User and kit request data.
- `sender_stand_request.py`: Functions for sending HTTP requests.
- `create_kit_name_kit_test.py`: Nine automated API test cases and assertion helpers.
- `.gitignore`: Excludes temporary Python and pytest files.
- `README.md`: Project overview and execution instructions.

## Requirements

- Python 3
- An active TripleTen Urban Grocers training server
- Internet access

## Installation

Clone the repository:

```bash
git clone https://github.com/GGO88-German/qa-project-Urban-Grocers-app-es.git
cd qa-project-Urban-Grocers-app-es
```

Install the dependencies:

```bash
python -m pip install pytest requests
```

## Configuration

Start the Urban Grocers training server and update `URL_SERVICE` in `configuration.py` with its current base URL.

Training-server URLs expire. A server connection error does not by itself indicate a product defect.

## Running the Tests

Run this command from the repository directory:

```bash
python -m pytest -v create_kit_name_kit_test.py
```

To save a JUnit XML report:

```bash
python -m pytest -v create_kit_name_kit_test.py --junitxml=results.xml
```

## Documented Findings

A previously recorded execution produced five passing tests and four failing tests.

The failing scenarios involved an empty name, an oversized name, a missing name, and a numeric value instead of a string.

Examples of observed discrepancies:

- An empty name returned 201 instead of the expected 400.
- A name with 512 characters returned 201 instead of 400.
- A request without `name` returned 500 instead of 400.

These are historical observations from the training environment, not results from a new execution. Run the suite against an active server to obtain current results.

Failed assertions should be investigated by comparing the requirements, request data, and actual response. Expected results should not be changed solely to make a test pass.

## Skills Demonstrated

- API test design
- Boundary-value analysis
- Positive and negative testing
- Authentication handling
- Reusable test helpers
- HTTP status and response-body validation
- Analysis of expected versus actual behavior

## Author

German Gonzalez Oregel

LinkedIn: https://www.linkedin.com/in/german-gonzalez-oregel-729a0243/

## Educational Context

This project uses the Urban Grocers training application and starter materials provided by TripleTen.
