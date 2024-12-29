from phone_number_validator.validator import PhoneNumberValidator

validator = PhoneNumberValidator()
is_valid = validator.validate("+447827156679")
response = validator._make_api_call("+447827156679")
full_response = validator.complete_response("+447827156679")
