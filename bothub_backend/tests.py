import unittest
import requests_mock

from bothub_backend.bothub import *


BOTHUB_API_URL = "https://api.bothub.it"
BOTHUB_API_REPOSITORY_NLP_URL = f"{BOTHUB_API_URL}/v2/repository/nlp"


class TestBothubBackend(unittest.TestCase):
    def setUp(self):
        self.bh = BothubBackend(backend=BOTHUB_API_URL)
        self.repository_authorization = "e25d890d-0746-47d1-8151-9fd9355cd913"  # Fake uuid
        self.language = "pt-br"
        self.repository_version = 50

    @requests_mock.Mocker()
    def test_request_backend_evaluate(self, request_mock):
        query_params = f"?language={self.language}&repository_version={self.repository_version}"
        url = f"{BOTHUB_API_REPOSITORY_NLP_URL}/authorization/evaluate/{self.repository_authorization}/{query_params}"
        json = {
            "update": True,
            "repository_version": 50,
            "language": "pt-br",
            "user_id": 1,
            "algorithm": "transformer_network_diet_bert",
            "use_name_entities": False,
            "use_competing_intents": False,
            "use_analyze_char": False
        }
        request_mock.get(url=url, json=json)

        response = self.bh.request_backend_evaluate(
            repository_authorization=self.repository_authorization,
            language=self.language,
            repository_version=self.repository_version,
        )

        self.assertEqual(response, json)

    @requests_mock.Mocker()
    def test_request_backend_info(self, request_mock):
        query_params = f"?language={self.language}&repository_version={self.repository_version}"
        url = f"{BOTHUB_API_REPOSITORY_NLP_URL}/authorization/info/{self.repository_authorization}/{query_params}"
        json = {"intents": ["comprar", "alugar"]}
        request_mock.get(url=url, json=json)

        response = self.bh.request_backend_info(
            repository_authorization=self.repository_authorization,
            language=self.language,
            repository_version=self.repository_version,
        )

        self.assertEqual(response, json)

    @requests_mock.Mocker()
    def test_request_backend_train(self, request_mock):
        query_params = f"?language={self.language}&repository_version={self.repository_version}"
        url = f"{BOTHUB_API_REPOSITORY_NLP_URL}/authorization/train/{self.repository_authorization}/{query_params}"
        json = {
            "ready_for_train": True,
            "current_version_id": 50,
            "repository_authorization_user_id": 1,
            "language": "pt-br",
            "algorithm": "transformer_network_diet_bert",
            "use_name_entities": False,
            "use_competing_intents": False,
            "use_analyze_char": False
        }
        request_mock.get(url=url, json=json)

        response = self.bh.request_backend_train(
            repository_authorization=self.repository_authorization,
            language=self.language,
            repository_version=self.repository_version,
        )

        self.assertEqual(response, json)
