from prefect import flow, task
import random


def unreliable_service():
    choices = ["a", "b", "ruh roh"]
    res = random.choice(choices)
    if res == "a" or res == "b":
        return res
    else:
        print("Service failed")
        raise Exception("Our unreliable service failed")

def only_with_a():
    print("Hey! You got 'a' as a result!")

def hope_our_service_worked(service_result, n):
    augmented_result = service_result*n
    print(f"Your result was {augmented_result}")

def flow_run(n):
    res = unreliable_service()
    if res == "a":
        only_with_a()
    hope_our_service_worked(res, n)

if __name__ == "__main__":
    flow_run(2)