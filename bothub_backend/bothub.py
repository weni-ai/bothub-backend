import time

import requests
import base64
from .backend import BaseBackend


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
        self, router, repository_authorization, language=None, repository_version=None
    ):
        print(f"Starting connection request_backend_parse()")
        time_start = time.time()
        if repository_version:
            version = requests.get(
                "{}/v2/repository/nlp/authorization/{}/{}/?language={}&repository_version={}".format(
                    self.backend, router, repository_authorization, language, repository_version
                ),
                headers={"Authorization": "Bearer {}".format(repository_authorization)},
            ).json()
        else:
            version = requests.get(
                "{}/v2/repository/nlp/authorization/{}/{}/?language={}".format(
                    self.backend, router, repository_authorization, language
                ),
                headers={"Authorization": "Bearer {}".format(repository_authorization)},
            ).json()
        print(f"End connection request_backend_parse() {str(time.time() - time_start)}")
        return version

    def request_backend_parse_nlu(self, update_id, repository_authorization):
        print(f"Starting connection request_backend_parse_nlu()")
        time_start = time.time()
        update = requests.get(
            "{}/v2/repository/nlp/update_interpreters/{}/".format(
                self.backend, update_id
            ),
            headers={"Authorization": "Bearer {}".format(repository_authorization)},
        ).json()
        print(
            f"End connection request_backend_parse_nlu() {str(time.time() - time_start)}"
        )
        return update

    def request_backend_start_training_nlu(
        self, update_id, by, repository_authorization
    ):
        print(f"Starting connection request_backend_start_training_nlu()")
        time_start = time.time()
        update = requests.post(
            "{}/v2/repository/nlp/authorization/train/start_training/".format(
                self.backend
            ),
            data={"repository_version": update_id, "by_user": by},
            headers={"Authorization": "Bearer {}".format(repository_authorization)},
        ).json()
        print(
            f"End connection request_backend_start_training_nlu() {str(time.time() - time_start)}"
        )
        return update

    def request_backend_get_entities_and_labels_nlu(
        self, repository_version, language, data, repository_authorization
    ):
        print(f"Starting connection request_backend_get_entities_and_labels_nlu()")
        time_start = time.time()
        update = requests.get(
            "{}/v2/repository/nlp/authorization/train/get_entities_and_labels/?repository_version={}&language={}".format(
                self.backend, repository_version, language
            ),
            data=data,
            headers={
                "Authorization": "Bearer {}".format(repository_authorization),
                "Content-Type": "application/json",
            },
        ).json()
        print(
            f"End connection request_backend_get_entities_and_labels_nlu() {str(time.time() - time_start)}"
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

    def request_backend_parse_nlu_persistor(self, update_id, repository_authorization):
        print(f"Starting connection request_backend_parse_nlu_persistor()")
        time_start = time.time()
        update = requests.get(
            "{}/v2/repository/nlp/update_interpreters/{}/".format(
                self.backend, update_id
            ),
            headers={"Authorization": "Bearer {}".format(repository_authorization)},
        ).json()
        print(
            f"End connection request_backend_parse_nlu_persistor() {str(time.time() - time_start)}"
        )
        return update

    def send_training_backend_nlu_persistor(
        self, update_id, botdata, repository_authorization
    ):
        print(f"Starting connection send_training_backend_nlu_persistor()")
        time_start = time.time()
        update = requests.post(
            "{}/v2/repository/nlp/update_interpreters/".format(self.backend),
            data={
                "id": update_id,
                "bot_data": base64.b64encode(botdata).decode("utf8"),
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
