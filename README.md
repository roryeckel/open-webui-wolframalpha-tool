# open-webui-wolframalpha-tool
Provides an interface for LLMs to query the WolframAlpha short answer text API in Open WebUI. Useful for Ollama!

First, set the environment variable of WOLFRAMALPHA_APP_ID with the app ID from your WolframAlpha developer portal and restart Open WebUI. Paste the contents of tools.py into your Open WebUI Workspace's Tools. Then, you can enable the tool for a query and ask the LLM about some real time information.

Note that the "Simple" response is refreshed whenever you visit the page again. That's why the time looks a bit off in this example :)

![Example Screenshot](./Example.png)
