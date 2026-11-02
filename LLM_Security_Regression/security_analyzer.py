import json

def load_results(path):

    with open(path, "r") as file:
        return json.load(file)


def calculate_asr(data):

    total = data["total_tests"]
    failed = data["failed_defense"]

    if total <= 0 or failed < 0 or failed > total:
        raise ValueError("Invalid test results")

    return (failed / total) * 100


def compare_security(baseline, current):

    results = {}

    if set(baseline) != set(current):
        raise ValueError("Test categories do not match")

    for category in baseline:

        old_asr = calculate_asr(
            baseline[category]
        )

        new_asr = calculate_asr(
            current[category]
        )

        difference = new_asr - old_asr

        results[category] = {
            "baseline_asr": old_asr,
            "current_asr": new_asr,
            "difference": difference,
            "regression": difference > 0
        }

    return results

if __name__ == "__main__":

    baseline = load_results("data/baseline.json")
    current = load_results("data/current.json")

    results = compare_security(baseline, current)

    for category, result in results.items():

        print(f"\nCategory: {category}")
        print(f"Baseline ASR: {result['baseline_asr']:.2f}%")
        print(f"Current ASR: {result['current_asr']:.2f}%")
        print(f"Difference: {result['difference']:+.2f}%")
        print(f"Regression: {result['regression']}")