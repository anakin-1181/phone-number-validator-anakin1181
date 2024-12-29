import requests


class PhoneNumberValidator:
    def __init__(self) -> None:
        self.api_key = "num_live_9ypNJRX0x5RzLuItJQfDXpej3ZbmV2fnqDBDWpE7"
        self.api_url = "https://api.numlookupapi.com/v1/validate/"

    def _make_api_call(self, phone_num: str, country_code: str = None):
        params = {"apikey": self.api_key}
        if country_code:
            params["country_code"] = country_code
        response = requests.get(self.api_url + phone_num, params=params)
        return response

    def validate(self, phone_num: str, country_code: str = None) -> bool:
        if not phone_num:
            raise ValueError("Phone Number cannot be empty.")
        response = self._make_api_call(phone_num, country_code)
        if response.ok:
            return response.json()["valid"]
        else:
            response.raise_for_status()

    def complete_response(self, phone_num: str, country_code: str = None):
        return self._make_api_call(phone_num, country_code=None).json()
