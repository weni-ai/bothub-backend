import time


def print_execution_time(function):
    def wrapper(*args, **kwargs):
        print(f"Starting connection {function.__name__}()")
        time_start = time.time()

        response = function(*args, **kwargs)

        print(f"End connection {function.__name__}() {str(time.time() - time_start)}")

        return response
    return wrapper
