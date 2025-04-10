import json


class Checker:
    def __init__(self, file_name):
        file_stem = file_name.split(".")[0]
        with open(f"{file_stem}.json", "r") as f:
            self.test_cases = json.load(f)

    def check(self, func):
        for i, case in enumerate(self.test_cases):
            result = func(**case["inputs"])
            assert result == case["output"]
            print(f"Case {i} passed, {case['inputs']} -> {result}")
