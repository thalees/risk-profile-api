# Risk Profile API

API to determine a user's risk profile for certain information

## Description

When submitting the correct user information, the risk analysis is performed and then apply an insurance plan ("economic", "regular", "responsible") corresponding to your risk profile.

## Getting Started

### Dependencies

* Flask
* Marshmallow
* Pytest
* pip3

### Installing

* After cloning that repository, create a **virtualenv** and activate:
```
virtualenv venv && . venv/bin/activate
```

* Finally install the necessary dependencies::
```
pip3 install -r requirements.txt
```

### Executing program

* To run this project, just execute the command below and the API will be working on _localhost:5000_
```
python3 routes.py run
```

### Tests

* To execute the project tests, simply run the command below:
```
pytest
```

**Api**
----

* **URL**

  `/risk-profile`

* **Method:**

  `POST`

* **Data Params**

  _The requisition data must follow this format, the fields being mandatory: `age`, `dependents`, `income`, `marital_status` and `risk_questions`_

  ```
  {
    "age": 35,
    "dependents": 2,
    "house": {"ownership_status": "owned"},
    "income": 0,
    "marital_status": "married",
    "risk_questions": [0, 1, 0],
    "vehicle": {"year": 2018}
  }
  ```

* **Success Response:**

  * **Code:** 201 <br />
    **Content**

  ```
  {
    "auto": "regular",
    "disability": "ineligible",
    "home": "economic",
    "life": "regular"
  }
  ```

* **Error Response:**

  * **Code:** 400 BAD REQUEST <br />
    **Content:**

  ```
  {
    "code": 400,
    "message": {
      "income": [
        "Missing data for required field."
      ]
    }
  }
  ```

  OR

  * **Code:** 422 UNPROCESSABLE ENTRY <br />
    **Content:**

  ```
  {
    "code": 422,
    "message": "age must be equals or greater than zero."
  }
  ```
