import requests

BASE_URL = "https://pi.crunchdao.com/api"

def submit_prompt(prompt_text):
    """
    Submit a prompt to the API and retrieve a prompt identifier.
    """
    url = f"{BASE_URL}/prompts"
    payload = {
        "prompt": prompt_text
    }
    response = requests.post(url, json=payload)
    response.raise_for_status()
    data = response.json()
    # Assume the response looks like: { "prompt_id": "abc123" }
    return data.get("prompt_id")

def get_time_series_scores(prompt_id):
    """
    Retrieve the time-series of scores for a given prompt_id.
    """
    url = f"{BASE_URL}/prompts/{prompt_id}/scores"
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()
    # Assume the response looks like: 
    # { 
    #   "prompt_id": "abc123", 
    #   "scores": [
    #       {"time": "2024-12-16T00:00:00Z", "value": 0.45},
    #       {"time": "2024-12-17T00:00:00Z", "value": 0.47}
    #   ]
    # }
    return data

def broadcast_prompt(prompt_text):
    """
    Make a 'broadcast' call with a prompt and receive a prompt identifier in response.
    """
    url = f"{BASE_URL}/prompts/broadcast"
    payload = {
        "prompt": prompt_text
    }
    response = requests.post(url, json=payload)
    response.raise_for_status()
    data = response.json()
    # Assume the response looks like: { "prompt_id": "def456" }
    return data.get("prompt_id")

def get_analysis_results(prompt_id):
    """
    Retrieve the results of the analysis, which includes:
    - A collection of records with (time, prompt_id, value, announce_id)
    - A list of recommended tickers
    """
    url = f"{BASE_URL}/results/{prompt_id}"
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()
    # Assume the response looks like:
    # {
    #   "prompt_id": "def456",
    #   "records": [
    #       {"time": "2024-12-16T00:00:00Z", "prompt_id": "def456", "value": 0.52, "announce_id": "ann123"},
    #       {"time": "2024-12-17T00:00:00Z", "prompt_id": "def456", "value": 0.50, "announce_id": "ann124"}
    #   ],
    #   "recommended_tickers": ["AAPL", "GOOGL", "AMZN"]
    # }
    return data

# Example usage of the above functions:
if __name__ == "__main__":
    # Submit a prompt and get a prompt_id
    prompt_id = submit_prompt("Analyze market sentiment for tech stocks.")
    print(f"Prompt ID from submission: {prompt_id}")

    # Retrieve time-series scores for the prompt
    scores = get_time_series_scores(prompt_id)
    print("Time-series scores:", scores)

    # Broadcast a prompt and get a prompt_id
    broadcasted_prompt_id = broadcast_prompt("Broadcast analysis for fintech sector.")
    print(f"Broadcasted Prompt ID: {broadcasted_prompt_id}")

    # Retrieve analysis results
    results = get_analysis_results(broadcasted_prompt_id)
    print("Analysis results:", results)
