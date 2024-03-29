import time

import requests
import base64
from .backend import BaseBackend
from .decorators import print_execution_time


class BothubBackend(BaseBackend):
    """
    Bothub instance as a backend
    """

    @print_execution_time
    def request_backend_start_evaluation(self, update_id, repository_authorization):
        url = f"{self.backend}/v2/repository/nlp/authorization/evaluate/evaluations/"
        query_params = {"repository_version": update_id}
        headers = {"Authorization": f"Bearer {repository_authorization}"}
        response = requests.get(url, params=query_params, headers=headers).json()

        return response

    @print_execution_time
    def request_backend_create_evaluate_results(self, data, repository_authorization):
        url = (
            f"{self.backend}/v2/repository/nlp/authorization/evaluate/evaluate_results/"
        )
        headers = {"Authorization": f"Bearer {repository_authorization}"}
        response = requests.post(url, data=data, headers=headers).json()

        return response

    @print_execution_time
    def request_backend_create_evaluate_results_intent(
        self, data, repository_authorization
    ):
        url = f"{self.backend}/v2/repository/nlp/authorization/evaluate/evaluate_results_intent/"
        headers = {"Authorization": f"Bearer {repository_authorization}"}
        response = requests.post(url, data=data, headers=headers).json()

        return response

    @print_execution_time
    def request_backend_create_evaluate_results_score(
        self, data, repository_authorization
    ):
        url = f"{self.backend}/v2/repository/nlp/authorization/evaluate/evaluate_results_score/"
        headers = {"Authorization": f"Bearer {repository_authorization}"}
        response = requests.post(url, data=data, headers=headers).json()

        return response

    @print_execution_time
    def get_langs(self):
        url = f"{self.backend}/v2/repository/nlp/authorization/langs/"
        response = requests.get(url).json()

        return response

    @print_execution_time
    def request_backend_parse(
        self, repository_authorization, language=None, repository_version=None
    ):
        url = f"{self.backend}/v2/repository/nlp/authorization/parse/{repository_authorization}/"
        query_params = {"language": language, "repository_version": repository_version}
        headers = {"Authorization": f"Bearer {repository_authorization}"}
        response = requests.get(url, params=query_params, headers=headers).json()

        return response

    @print_execution_time
    def request_backend_evaluate(
        self, repository_authorization, language=None, repository_version=None
    ):
        url = f"{self.backend}/v2/repository/nlp/authorization/evaluate/{repository_authorization}/"
        query_params = {"language": language, "repository_version": repository_version}
        headers = {"Authorization": f"Bearer {repository_authorization}"}
        response = requests.get(url, params=query_params, headers=headers).json()

        return response

    @print_execution_time
    def request_backend_info(
        self, repository_authorization, repository_version_id=None, repository_version_language_id=None
    ):
        url = f"{self.backend}/v2/repository/nlp/authorization/info/{repository_authorization}/"
        query_params = {
            "repository_version": repository_version_id,
            "repository_version_language": repository_version_language_id
        }
        headers = {"Authorization": f"Bearer {repository_authorization}"}
        response = requests.get(url, params=query_params, headers=headers).json()

        return response

    @print_execution_time
    def request_backend_train(
        self, repository_authorization, language=None, repository_version=None
    ):
        url = f"{self.backend}/v2/repository/nlp/authorization/train/{repository_authorization}/"
        query_params = {"language": language, "repository_version": repository_version}
        headers = {"Authorization": f"Bearer {repository_authorization}"}
        response = requests.get(url, params=query_params, headers=headers).json()

        return response

    @print_execution_time
    def request_all_readytotrain_languages(
        self, repository_authorization, repository_version=None
    ):
        url = f"{self.backend}/v2/repository/nlp/authorization/train-languages/{repository_authorization}/"
        params = {"repository_version": repository_version}
        headers = {"Authorization": f"Bearer {repository_authorization}"}
        response = requests.get(url, params=params, headers=headers).json()

        return response

    @print_execution_time
    def request_backend_start_training_nlu(
        self, update_id, by, repository_authorization, from_queue
    ):
        url = f"{self.backend}/v2/repository/nlp/authorization/train/start_training/"
        data = {
            "repository_version": update_id,
            "by_user": by,
            "from_queue": from_queue,
        }
        headers = {"Authorization": f"Bearer {repository_authorization}"}
        response = requests.post(url, data=data, headers=headers).json()

        return response

    @print_execution_time
    def request_backend_save_queue_id(
        self, update_id, repository_authorization, task_id, from_queue, type_processing
    ):
        url = f"{self.backend}/v2/repository/nlp/authorization/train/save_queue_id/"
        data = {
            "repository_version": update_id,
            "task_id": task_id,
            "from_queue": from_queue,
            "type_processing": type_processing,
        }
        headers = {"Authorization": f"Bearer {repository_authorization}"}
        response = requests.post(url, data=data, headers=headers).json()

        return response

    @print_execution_time
    def request_backend_get_examples(
        self, update_id, page=None, repository_authorization=None, intent=""
    ):
        headers = {"Authorization": f"Bearer {repository_authorization}"}
        if page:
            response = requests.get(page, headers=headers).json()
        else:
            url = f"{self.backend}/v2/repository/nlp/authorization/train/get_examples/"
            query_params = {"repository_version": update_id, "intent": intent}
            response = requests.get(url, params=query_params, headers=headers).json()

        return response

    @print_execution_time
    def request_backend_trainfail_nlu(self, update_id, repository_authorization):
        url = f"{self.backend}/v2/repository/nlp/authorization/train/train_fail/"
        data = {"repository_version": update_id}
        headers = {"Authorization": f"Bearer {repository_authorization}"}
        response = requests.post(url, data=data, headers=headers).json()

        return response

    @print_execution_time
    def request_backend_traininglog_nlu(
        self, update_id, training_log, repository_authorization
    ):
        url = f"{self.backend}/v2/repository/nlp/authorization/train/training_log/"
        data = {"repository_version": update_id, "training_log": training_log}
        headers = {"Authorization": f"Bearer {repository_authorization}"}
        response = requests.post(url, data=data, headers=headers).json()

        return response

    @print_execution_time
    def request_backend_parse_nlu_persistor(
        self, update_id, repository_authorization, rasa_version, no_bot_data=None
    ):
        url = f"{self.backend}/v2/repository/nlp/update_interpreters/{update_id}/"
        query_params = {"rasa_version": rasa_version, "no_bot_data": no_bot_data}
        headers = {"Authorization": f"Bearer {repository_authorization}"}
        response = requests.get(url, params=query_params, headers=headers).json()

        return response

    @print_execution_time
    def send_training_backend_nlu_persistor(
        self, update_id, botdata, repository_authorization, rasa_version
    ):
        url = f"{self.backend}/v2/repository/nlp/update_interpreters/"
        data = {
            "id": update_id,
            "bot_data": base64.b64encode(botdata).decode("utf8"),
            "rasa_version": rasa_version,
        }
        headers = {"Authorization": f"Bearer {repository_authorization}"}
        response = requests.post(url, data=data, headers=headers).json()

        return response

    @print_execution_time
    def request_backend_repository_entity_nlu_parse(
        self, update_id, repository_authorization, entity
    ):
        url = f"{self.backend}/v2/repository/nlp/authorization/parse/repository_entity/"
        query_params = {"repository_version": update_id, "entity": entity}
        headers = {"Authorization": f"Bearer {repository_authorization}"}
        response = requests.get(url, params=query_params, headers=headers).json()

        return response


    @print_execution_time
    def send_log_nlp_parse(self, data):
        url = f"{self.backend}/v2/repository/nlp/log/"
        headers = {"Content-Type": "application/json"}
        response = requests.post(url, json=data, headers=headers).json()

        return response


    @print_execution_time
    def send_log_qa_nlp_parse(self, data):
        url = f"{self.backend}/v2/repository/nlp/qa/log/"
        headers = {"Content-Type": "application/json"}
        response = requests.post(url, json=data, headers=headers).json()

        return response


    @print_execution_time
    def request_backend_get_current_configuration(self, repository_authorization):
        url = f"{self.backend}/v2/repository/nlp/authorization/info/{repository_authorization}/get_current_configuration"
        headers = {"Authorization": f"Bearer {repository_authorization}"}
        response = requests.get(url, headers=headers).json()

        return response

    def request_backend_knowledge_bases(
        self, repository_authorization, knowledge_base_id, language
    ):
        url = f"{self.backend}/v2/repository/nlp/authorization/knowledge-base/{repository_authorization}/"
        query_params = {"knowledge_base_id": knowledge_base_id, "language": language}
        headers = {"Authorization": f"Bearer {repository_authorization}"}
        response = requests.get(url, params=query_params, headers=headers).json()

        return response

    def request_backend_examples(
        self, repository_authorization, language, repository_version=None, page=None
    ):
        url = f"{self.backend}/v2/repository/nlp/authorization/examples/{repository_authorization}/"
        query_params = {"repository_version": repository_version, "language": language}
        headers = {"Authorization": f"Bearer {repository_authorization}"}
        if page:
            response = requests.get(page, headers=headers).json()
        else:
            response = requests.get(url, params=query_params, headers=headers).json()

        return response

    def request_backend_start_automatic_evaluate(
        self, repository_authorization, repository_version, language
    ):
        url = f"{self.backend}/v2/repository/nlp/authorization/automatic-evaluate/{repository_authorization}/"
        query_params = {"repository_version": repository_version, "language": language}
        headers = {"Authorization": f"Bearer {repository_authorization}"}
        response = requests.get(url, params=query_params, headers=headers).json()

        return response
