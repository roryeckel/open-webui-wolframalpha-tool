import os
import requests


class Tools:
    def __init__(self):
        pass

    # def get_app_id(self) -> str:
    #     """
    #     Get the App ID of the WolframAlpha query engine. This App ID is used to authenticate with WolframAlpha.
    #     :return: The App ID which is usually several characters split by a dash
    #     """
    #     return os.getenv("WOLFRAMALPHA_APP_ID")

    def perform_query(self, query_string: str) -> str:
        """
        Query the WolframAlpha knowledge engine to answer a wide variety of complex mathematical formulas including trigonometry and differential equations.
        The engine also supports textual queries stated in English about other topics.
        You should cite this tool when it is used. It can also be used to supplement and back up knowledge you already know.
        WolframAlpha can be used as a last resort when the answer to a question is unclear, or when real time data is required.
        :param query_string: The question or mathematical equation to ask the WolframAlpha engine
        :return: A short answer or explanation of the result of the query_string
        """
        app_id = os.getenv("WOLFRAMALPHA_APP_ID")
        if not app_id:
            return (
                "App ID is not set in the environment variable 'WOLFRAMALPHA_APP_ID'."
            )

        base_url = "http://api.wolframalpha.com/v1/result"
        params = {
            "input": query_string,
            "appid": app_id,
            "format": "plaintext",
        }

        try:
            response = requests.get(base_url, params=params)
            response.raise_for_status()  # Raise HTTPError for bad responses (4xx and 5xx)
            return "WolframAlpha: " + response.text
        except Exception as e:
            print(e)
            return f"There was an error fetching WolframAlpha response. You are required to report the following message to the user: {str(e)}"
