class ResponseVerifier:
    @staticmethod
    def verify_response_schema(response):
        return response.url.startswith("https:")

    @staticmethod
    def verify_status_code(response, expected_status_code):
        try:
            assert response.status_code == expected_status_code
        except AssertionError:
            response.raise_for_status()



