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
    def test_request_backend_start_evaluation(self, request_mock):
        query_params = f"?repository_version={self.repository_version}"
        url = f"{BOTHUB_API_REPOSITORY_NLP_URL}/authorization/evaluate/evaluations/{query_params}"
        json = [
            {
                "text": "quero comprar um chocolate",
                "intent": "comprar",
                "entities": ["comida"]
            },
            {
                "text": "quero comer um chocolate",
                "intent": "comer",
                "entities": ["comida"]
            }
        ]
        request_mock.get(url=url, json=json)

        response = self.bh.request_backend_start_evaluation(
            update_id=self.repository_version,
            repository_authorization=self.repository_authorization
        )

        self.assertEqual(response, json)

    @requests_mock.Mocker()
    def test_request_backend_create_evaluate_results(self, request_mock):
        url = f"{BOTHUB_API_REPOSITORY_NLP_URL}/authorization/evaluate/evaluate_results/"
        json = {
            "evaluate_id": 5,
            "evaluate_version": 3
        }
        request_mock.post(url=url, json=json)

        data = {
            "repository_version": 46,
            "intentprecision": 1,
            "intentf1_score": 1,
            "intentaccuracy": 1,
            "entityprecision": 1,
            "entityf1_score": 1,
            "entityaccuracy": 1,
            "matrix_chart": "teste",
            "confidence_chart": "teste",
            "log": "teste",
            "cross_validation": False
        }

        response = self.bh.request_backend_create_evaluate_results(
            data=data,
            repository_authorization=self.repository_authorization
        )

        self.assertEqual(response, json)

    @requests_mock.Mocker()
    def test_request_backend_create_evaluate_results_intent(self, request_mock):
        url = f"{BOTHUB_API_REPOSITORY_NLP_URL}/authorization/evaluate/evaluate_results_intent/"
        json = {}
        request_mock.post(url=url, json=json)

        data = {
            "evaluate_id": 1,
            "precision": 1,
            "recall": 1,
            "f1_score": 1,
            "support": 1,
            "intent_key": "eletros"
        }

        response = self.bh.request_backend_create_evaluate_results_intent(
            data=data,
            repository_authorization=self.repository_authorization
        )

        self.assertEqual(response, json)

    @requests_mock.Mocker()
    def test_request_backend_create_evaluate_results_score(self, request_mock):
        url = f"{BOTHUB_API_REPOSITORY_NLP_URL}/authorization/evaluate/evaluate_results_score/"
        json = {}
        request_mock.post(url=url, json=json)

        data = {
            "evaluate_id": 1,
            "repository_version": 46,
            "precision": 1,
            "recall": 1,
            "f1_score": 1,
            "support": 1,
            "intent_key": "entidade_teste"
        }

        response = self.bh.request_backend_create_evaluate_results_score(
            data=data,
            repository_authorization=self.repository_authorization
        )

        self.assertEqual(response, json)

    @requests_mock.Mocker()
    def test_get_langs(self, request_mock):
        url = f"{BOTHUB_API_REPOSITORY_NLP_URL}/authorization/langs/"
        json = {
            "english": [
                "en"
            ],
            "portuguese": [
                "pt",
                "pt_br"
            ]
        }
        request_mock.get(url=url, json=json)

        response = self.bh.get_langs()

        self.assertEqual(response, json)

    @requests_mock.Mocker()
    def test_request_backend_parse(self, request_mock):
        query_params = f"?language={self.language}&repository_version={self.repository_version}"
        url = f"{BOTHUB_API_REPOSITORY_NLP_URL}/authorization/parse/{self.repository_authorization}/{query_params}"
        json = {
            "version": True,
            "repository_version": 50,
            "total_training_end": 0,
            "language": "pt-br",
            "algorithm": "transformer_network_diet_bert",
            "use_name_entities": False,
            "use_competing_intents": False,
            "use_analyze_char": False
        }
        request_mock.get(url=url, json=json)

        response = self.bh.request_backend_parse(
            repository_authorization=self.repository_authorization,
            language=self.language,
            repository_version=self.repository_version,
        )

        self.assertEqual(response, json)

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

    @requests_mock.Mocker()
    def test_request_backend_start_training_nlu(self, request_mock):
        url = f"{BOTHUB_API_REPOSITORY_NLP_URL}/authorization/train/start_training/"
        json = {
            "language": "en",
            "repository_version": 47,
            "repository_uuid": "544ddd17-cd8d-4280-972e-5c56c69a635e",
            "intent": [4, 5],
            "algorithm": "transformer_network_diet_bert",
            "use_name_entities": False,
            "use_competing_intents": False,
            "use_analyze_char": True,
            "total_training_end": 6
        }
        request_mock.post(url=url, json=json)

        response = self.bh.request_backend_start_training_nlu(
            update_id=self.repository_version,
            by=1,
            repository_authorization=self.repository_authorization,
            from_queue="celery",
        )

        self.assertEqual(response, json)

    @requests_mock.Mocker()
    def test_request_backend_save_queue_id(self, request_mock):
        url = f"{BOTHUB_API_REPOSITORY_NLP_URL}/authorization/train/save_queue_id/"
        json = [
            {
                "id": 1,
                "id_queue": 1,
                "from_queue": 1,
                "status": 1,
                "ml_units": 1,
                "created_at": 1,
                "end_training": 1,
                "status_codes": 1,
                "from_queue_codes": 1,
                "type_processing": 1,
                "processing_codes": 1
            }
        ]
        request_mock.post(url=url, json=json)

        response = self.bh.request_backend_save_queue_id(
            update_id=self.repository_version,
            repository_authorization=self.repository_authorization,
            task_id=1,
            from_queue="celery",
            type_processing=1
        )

        self.assertEqual(response, json)

    @requests_mock.Mocker()
    def test_request_backend_get_examples(self, request_mock):
        query_params = f"?repository_version={self.repository_version}"
        url = f"{BOTHUB_API_REPOSITORY_NLP_URL}/authorization/train/get_examples/{query_params}"
        json = {
            "count": 1,
            "next": None,
            "previous": None,
            "results": [
                {
                    "text": "adquirir um apartamento",
                    "intent": "comprar",
                    "entities": [
                        {
                            "start": 12,
                            "end": 23,
                            "value": "apartamento",
                            "entity": "moradia"
                        }
                    ]
                }
            ]
        }
        request_mock.get(url=url, json=json)

        response = self.bh.request_backend_get_examples(
            update_id=self.repository_version,
            repository_authorization=self.repository_authorization
        )

        self.assertEqual(response, json)

    @requests_mock.Mocker()
    def test_request_backend_trainfail_nlu(self, request_mock):
        url = f"{BOTHUB_API_REPOSITORY_NLP_URL}/authorization/train/train_fail/"
        json = {}
        request_mock.post(url=url, json=json)

        response = self.bh.request_backend_trainfail_nlu(
            update_id=self.repository_version,
            repository_authorization=self.repository_authorization
        )

        self.assertEqual(response, json)

    @requests_mock.Mocker()
    def test_request_backend_traininglog_nlu(self, request_mock):
        url = f"{BOTHUB_API_REPOSITORY_NLP_URL}/authorization/train/training_log/"
        json = {}
        request_mock.post(url=url, json=json)

        response = self.bh.request_backend_traininglog_nlu(
            update_id=self.repository_version,
            training_log={},
            repository_authorization=self.repository_authorization
        )

        self.assertEqual(response, json)

    @requests_mock.Mocker()
    def test_request_backend_parse_nlu_persistor(self, request_mock):
        query_params = f"?rasa_version=1"
        url = f"{BOTHUB_API_REPOSITORY_NLP_URL}/update_interpreters/{self.repository_version}/{query_params}"
        json = {}
        request_mock.get(url=url, json=json)

        response = self.bh.request_backend_parse_nlu_persistor(
            update_id=self.repository_version,
            repository_authorization=self.repository_authorization,
            rasa_version="1"
        )

        self.assertEqual(response, json)

    @requests_mock.Mocker()
    def test_send_training_backend_nlu_persistor(self, request_mock):
        url = f"{BOTHUB_API_REPOSITORY_NLP_URL}/update_interpreters/"
        json = {}
        request_mock.post(url=url, json=json)

        response = self.bh.send_training_backend_nlu_persistor(
            update_id=self.repository_version,
            botdata=b"testbyte",
            repository_authorization=self.repository_authorization,
            rasa_version="1.10.6"
        )

        self.assertEqual(response, json)

    @requests_mock.Mocker()
    def test_request_backend_repository_entity_nlu_parse(self, request_mock):
        query_params = f"?repository_version={self.repository_version}&entity=eletrodomestico"
        url = f"{BOTHUB_API_REPOSITORY_NLP_URL}/authorization/parse/repository_entity/{query_params}"
        json = {
            "label": True,
            "label_value": "teste"
        }
        request_mock.get(url=url, json=json)

        response = self.bh.request_backend_repository_entity_nlu_parse(
            update_id=self.repository_version,
            repository_authorization=self.repository_authorization,
            entity="eletrodomestico"
        )

        self.assertEqual(response, json)

    @requests_mock.Mocker()
    def test_send_log_nlp_parse(self, request_mock):
        url = f"{BOTHUB_API_URL}/v2/repository/nlp/log/"
        json = {
            "id": 1,
            "text": "test",
            "user_agent": "test",
            "repository_version_language": "test",
            "nlp_log": "test",
            "user": "test",
            "log_intent": "test",
            "from_backend": "test",
        }
        request_mock.post(url=url, json=json)

        data = {
            "text": "test",
            "from_backend": False,
            "user_agent": "PostmanRuntime/7.26.10",
            "user": "teste"
        }

        response = self.bh.send_log_nlp_parse(data=data)

        self.assertEqual(response, json)

        data = {
            "text": "test",
            "from_backend": False,
            "user_agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) " + 
                            "Chrome/87.0.4280.88 Safari/537.36",
            "user": "teste"
        }

        response = self.bh.send_log_nlp_parse(data=data)

        self.assertEqual(response, json)

    @requests_mock.Mocker()
    def test_request_backend_get_current_configuration(self, request_mock):
        url = f"{BOTHUB_API_REPOSITORY_NLP_URL}/authorization/info/{self.repository_authorization}/get_current_configuration"
        json = {
            "language": self.language,
            "user_id": 979,
            "algorithm": "transformer_network_diet_bert",
            "use_name_entities": False,
            "use_competing_intents": False,
            "use_analyze_char": False
        }
        request_mock.get(url=url, json=json)

        response = self.bh.request_backend_get_current_configuration(
            repository_authorization=self.repository_authorization,
        )

        self.assertEqual(response, json)

    @requests_mock.Mocker()
    def test_request_backend_knowledge_bases(self, request_mock):
        query_params = f"?knowledge_base_id=1&language={self.language}"
        url = f"{BOTHUB_API_REPOSITORY_NLP_URL}/authorization/knowledge-base/{self.repository_authorization}/{query_params}"
        json = {
            "knowledge_base_id": 1,
            "text": "a weni é uma empresa sensacional",
            "language": self.language 
        }
        request_mock.get(url=url, json=json)

        response = self.bh.request_backend_knowledge_bases(
            repository_authorization=self.repository_authorization,
            knowledge_base_id=1,
            language=self.language
        )

        self.assertEqual(response, json)

    @requests_mock.Mocker()
    def test_request_backend_examples(self, request_mock):
        query_params = f"?repository_version={self.repository_version}&language={self.language}"
        url = f"{BOTHUB_API_REPOSITORY_NLP_URL}/authorization/examples/{self.repository_authorization}/{query_params}"
        json = {
            "count": 4,
            "next": None,
            "previous": None,
            "results": [
                {
                    "text": "quer morar num ap alugado",
                    "intent": "alugar",
                    "entities": []
                },
                {
                    "text": "quero alugar casa",
                    "intent": "alugar",
                    "entities": []
                }
            ]
        }
        request_mock.get(url=url, json=json)

        response = self.bh.request_backend_examples(
            repository_authorization=self.repository_authorization,
            language=self.language,
            repository_version=self.repository_version
        )

        self.assertEqual(response, json)
