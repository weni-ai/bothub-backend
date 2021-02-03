import time

import requests
import base64
from .backend import BaseBackend
from .decorators import print_execution_time


class BothubBackend(BaseBackend):
    """
    Bothub instance as a backend
    """

    def request_backend_start_evaluation(self, update_id, repository_authorization):
        print(f"Starting connection request_backend_start_evaluation()")
        time_start = time.time()
        update = requests.get(
            "{}/v2/repository/nlp/authorization/evaluate/evaluations/?repository_version={}".format(
                self.backend, update_id
            ),
            headers={"Authorization": "Bearer {}".format(repository_authorization)},
        ).json()
        print(
            f"End connection request_backend_start_evaluation() {str(time.time() - time_start)}"
        )
        return update

    def request_backend_create_evaluate_results(self, data, repository_authorization):
        print(f"Starting connection request_backend_create_evaluate_results()")
        time_start = time.time()
        update = requests.post(
            "{}/v2/repository/nlp/authorization/evaluate/evaluate_results/".format(
                self.backend,
            ),
            data=data,
            headers={"Authorization": "Bearer {}".format(repository_authorization)},
        ).json()
        print(
            f"End connection request_backend_create_evaluate_results() {str(time.time() - time_start)}"
        )
        return update

    def request_backend_create_evaluate_results_intent(
        self, data, repository_authorization
    ):
        print(f"Starting connection request_backend_create_evaluate_results_intent()")
        time_start = time.time()
        update = requests.post(
            "{}/v2/repository/nlp/authorization/evaluate/evaluate_results_intent/".format(
                self.backend,
            ),
            data=data,
            headers={"Authorization": "Bearer {}".format(repository_authorization)},
        ).json()
        print(
            f"End connection request_backend_create_evaluate_results_intent() {str(time.time() - time_start)}"
        )
        return update

    def request_backend_create_evaluate_results_score(
        self, data, repository_authorization
    ):
        print(f"Starting connection request_backend_create_evaluate_results_score()")
        time_start = time.time()
        update = requests.post(
            "{}/v2/repository/nlp/authorization/evaluate/evaluate_results_score/".format(
                self.backend,
            ),
            data=data,
            headers={"Authorization": "Bearer {}".format(repository_authorization)},
        ).json()
        print(
            f"End connection request_backend_create_evaluate_results_score() {str(time.time() - time_start)}"
        )
        return update

    def get_langs(self):
        print(f"Starting connection get_langs()")
        time_start = time.time()
        langs = requests.get(
            "{}/v2/repository/nlp/authorization/langs/".format(self.backend,)
        ).json()
        print(f"End connection get_langs() {str(time.time() - time_start)}")
        return langs

    def request_backend_parse(
        self, repository_authorization, language=None, repository_version=None
    ):
        print(f"Starting connection request_backend_parse()")
        time_start = time.time()
        if repository_version:
            version = requests.get(
                "{}/v2/repository/nlp/authorization/parse/{}/?language={}&repository_version={}".format(
                    self.backend,
                    repository_authorization,
                    language,
                    repository_version,
                ),
                headers={"Authorization": "Bearer {}".format(repository_authorization)},
            ).json()
        else:
            version = requests.get(
                "{}/v2/repository/nlp/authorization/parse/{}/?language={}".format(
                    self.backend, repository_authorization, language
                ),
                headers={"Authorization": "Bearer {}".format(repository_authorization)},
            ).json()
        print(f"End connection request_backend_parse() {str(time.time() - time_start)}")
        return version

    def request_backend_evaluate(
        self, repository_authorization, language=None, repository_version=None
    ):
        print(f"Starting connection request_backend_evaluate()")
        time_start = time.time()
        if repository_version:
            version = requests.get(
                "{}/v2/repository/nlp/authorization/evaluate/{}/?language={}&repository_version={}".format(
                    self.backend,
                    repository_authorization,
                    language,
                    repository_version,
                ),
                headers={"Authorization": "Bearer {}".format(repository_authorization)},
            ).json()
        else:
            version = requests.get(
                "{}/v2/repository/nlp/authorization/evaluate/{}/?language={}".format(
                    self.backend, repository_authorization, language
                ),
                headers={"Authorization": "Bearer {}".format(repository_authorization)},
            ).json()
        print(
            f"End connection request_backend_evaluate() {str(time.time() - time_start)}"
        )
        return version

    @print_execution_time
    def request_backend_info(self, repository_authorization, language=None, repository_version=None):
        url = f"{self.backend}/v2/repository/nlp/authorization/info/{repository_authorization}/"
        query_params = {
            "language": language,
            "repository_version": repository_version
        }
        headers = {
            "Authorization": f"Bearer {repository_authorization}"
        }
        response = requests.get(url, params=query_params, headers=headers).json()

        return response

    @print_execution_time
    def request_backend_train(self, repository_authorization, language=None, repository_version=None):
        url = f"{self.backend}/v2/repository/nlp/authorization/train/{repository_authorization}/"
        query_params = {
            "language": language,
            "repository_version": repository_version
        }
        headers = {
            "Authorization": f"Bearer {repository_authorization}"
        }
        response = requests.get(url, params=query_params, headers=headers).json()

        return response

    def request_backend_start_training_nlu(
        self, update_id, by, repository_authorization, from_queue
    ):
        print(f"Starting connection request_backend_start_training_nlu()")
        time_start = time.time()
        update = requests.post(
            "{}/v2/repository/nlp/authorization/train/start_training/".format(
                self.backend
            ),
            data={"repository_version": update_id, "by_user": by, "from_queue": from_queue},
            headers={"Authorization": "Bearer {}".format(repository_authorization)},
        ).json()
        print(
            f"End connection request_backend_start_training_nlu() {str(time.time() - time_start)}"
        )
        return update

    def request_backend_save_queue_id(
        self, update_id, repository_authorization, task_id, from_queue
    ):
        print(f"Starting connection request_backend_save_queue_id()")
        time_start = time.time()
        update = requests.post(
            "{}/v2/repository/nlp/authorization/train/save_queue_id/".format(
                self.backend
            ),
            data={
                "repository_version": update_id,
                "task_id": task_id,
                "from_queue": from_queue,
            },
            headers={"Authorization": "Bearer {}".format(repository_authorization)},
        ).json()
        print(
            f"End connection request_backend_save_queue_id() {str(time.time() - time_start)}"
        )
        return update

    def request_backend_get_examples(
        self, update_id, use_pagination=False, page=None, repository_authorization=None
    ):
        print(f"Starting connection request_backend_get_examples()")
        time_start = time.time()
        if not use_pagination:
            update = requests.get(
                "{}/v2/repository/nlp/authorization/train/get_examples/?repository_version={}".format(
                    self.backend, update_id
                ),
                headers={"Authorization": "Bearer {}".format(repository_authorization)},
            ).json()
        else:
            update = requests.get(
                page,
                headers={"Authorization": "Bearer {}".format(repository_authorization)},
            ).json()
        print(
            f"End connection request_backend_get_examples() {str(time.time() - time_start)}"
        )

        return update

    def request_backend_get_examples_labels(
        self, update_id, use_pagination=False, page=None, repository_authorization=None
    ):
        print(f"Starting connection request_backend_get_examples_labels()")
        time_start = time.time()
        if not use_pagination:
            update = requests.get(
                "{}/v2/repository/nlp/authorization/train/get_examples_labels/?repository_version={}".format(
                    self.backend, update_id
                ),
                headers={"Authorization": "Bearer {}".format(repository_authorization)},
            ).json()
        else:
            update = requests.get(
                page,
                headers={"Authorization": "Bearer {}".format(repository_authorization)},
            ).json()
        print(
            f"End connection request_backend_get_examples_labels() {str(time.time() - time_start)}"
        )
        return update

    def request_backend_trainfail_nlu(self, update_id, repository_authorization):
        print(f"Starting connection request_backend_trainfail_nlu()")
        time_start = time.time()
        update = requests.post(
            "{}/v2/repository/nlp/authorization/train/train_fail/".format(self.backend),
            data={"repository_version": update_id},
            headers={"Authorization": "Bearer {}".format(repository_authorization)},
        ).json()
        print(
            f"End connection request_backend_trainfail_nlu() {str(time.time() - time_start)}"
        )
        return update

    def request_backend_traininglog_nlu(
        self, update_id, training_log, repository_authorization
    ):
        print(f"Starting connection request_backend_traininglog_nlu()")
        time_start = time.time()
        update = requests.post(
            "{}/v2/repository/nlp/authorization/train/training_log/".format(
                self.backend
            ),
            data={"repository_version": update_id, "training_log": training_log},
            headers={"Authorization": "Bearer {}".format(repository_authorization)},
        ).json()
        print(
            f"End connection request_backend_traininglog_nlu() {str(time.time() - time_start)}"
        )
        return update

    def request_backend_parse_nlu_persistor(
            self, update_id, repository_authorization, rasa_version, no_bot_data=False
    ):
        print(f"Starting connection request_backend_parse_nlu_persistor()")
        time_start = time.time()

        if no_bot_data:
            update = requests.get(
                "{}/v2/repository/nlp/update_interpreters/{}/?rasa_version={}?no_bot_data={}".format(
                    self.backend, update_id, rasa_version, no_bot_data
                ),
                headers={"Authorization": "Bearer {}".format(repository_authorization)},
            ).json()
        else:
            update = requests.get(
                "{}/v2/repository/nlp/update_interpreters/{}/?rasa_version={}".format(
                    self.backend, update_id, rasa_version
                ),
                headers={"Authorization": "Bearer {}".format(repository_authorization)},
            ).json()

        print(
            f"End connection request_backend_parse_nlu_persistor() {str(time.time() - time_start)}"
        )
        return update

    def send_training_backend_nlu_persistor(
        self, update_id, botdata, repository_authorization, rasa_version
    ):
        print(f"Starting connection send_training_backend_nlu_persistor()")
        time_start = time.time()
        update = requests.post(
            "{}/v2/repository/nlp/update_interpreters/".format(self.backend),
            data={
                "id": update_id,
                "bot_data": base64.b64encode(botdata).decode("utf8"),
                "rasa_version": rasa_version,
            },
            headers={"Authorization": "Bearer {}".format(repository_authorization)},
        ).json()
        print(
            f"End connection send_training_backend_nlu_persistor() {str(time.time() - time_start)}"
        )
        return update

    def request_backend_repository_entity_nlu_parse(
        self, update_id, repository_authorization, entity
    ):
        print(f"Starting connection request_backend_repository_entity_nlu_parse()")
        time_start = time.time()
        update = requests.get(
            "{}/v2/repository/nlp/authorization/parse/repository_entity/?repository_version={}&entity={}".format(
                self.backend, update_id, entity
            ),
            headers={"Authorization": "Bearer {}".format(repository_authorization)},
        ).json()
        print(
            f"End connection request_backend_repository_entity_nlu_parse() {str(time.time() - time_start)}"
        )
        return update

    def send_log_nlp_parse(self, data):
        print(f"Starting connection send_log_nlp_parse()")
        time_start = time.time()
        update = requests.post(
            "{}/v2/repository/nlp/log/".format(self.backend),
            json=data,
            headers={"Content-Type": "application/json",},
        ).json()
        print(f"End connection send_log_nlp_parse() {str(time.time() - time_start)}")
        return update
