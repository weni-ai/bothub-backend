import unittest
import requests_mock

from bothub_backend.bothub import *


class TestBothubBackend(unittest.TestCase):
    def setUp(self):
        self.bh = BothubBackend(backend="https://api.bothub.it")
        self.repository_authorization = "e25d890d-0746-47d1-8151-9fd9355cd913"  # Fake uuid
        self.language = "pt-br"
        self.repository_version = 50

    @requests_mock.Mocker()
    def test_request_backend_info(self, request_mock):
        query_params = f"?language={self.language}&repository_version={self.repository_version}"
        url = f"https://api.bothub.it/v2/repository/nlp/authorization/info/{self.repository_authorization}/{query_params}"
        json = {"intents": ["comprar", "alugar"]}
        request_mock.get(url=url, json=json)

        response = self.bh.request_backend_info(
            repository_authorization=self.repository_authorization,
            language=self.language,
            repository_version=self.repository_version,
        )

        self.assertEqual(response, json)
