## Project Overview

This project is a Python-based phone number validator. It checks if a given phone number is valid using Numlookup api.

## Features

- Validate phone numbers
- Support for multiple phone number formats

## Installation

To install the required dependencies, run:

```bash
pip install poetry-plugin-export
```

```bash
pip install -i https://test.pypi.org/simple/ phone-number-validator-anakin1181
```

## Usage

To validate a phone number, use the following command:

```python
from phone_number_validator.validator import PhoneNumberValidator

validator = PhoneNumberValidator("<api_key>")
is_valid = validator.validate("<phone_number>")
```

Register an account on Numlookup api and replace `<api_key>` with an actual api

Replace `<phone_number>` with the actual phone number you want to validate.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request.

## License

This project is licensed under the MIT License.
