class ResponseVerifier:
    @staticmethod
    def check_response_status(response, expected_status_code):
        assert response.status_code == expected_status_code
