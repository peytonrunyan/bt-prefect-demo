from prefect import flow, task
import random


@task(retries=3, name="Unreliable Service")
def unreliable_service():
    choices = ["a", "b", "ruh roh"]
    res = random.choice(choices)
    if res == "a" or res == "b":
        return res
    else:
        print("Service failed")
        raise Exception("Our unreliable service failed")

@task
def only_with_a():
    print("Hey! You got 'a' as a result!")

@task(name="Final processing")
def hope_our_service_worked(service_result, n):
    augmented_result = service_result*n
    print(f"Your result was {augmented_result}")

@flow(name="lambda-flow")
def flow_run(n: int):
    res = unreliable_service()
    if res.result() == "a":         # We must a `.result()` to a prefect task
        only_with_a()               #   if we want use the result of the task
    hope_our_service_worked(res, n)    #   in the logic, instead of just passing
                                    #   the result to another task.
if __name__ == "__main__":
    flow_run(2)