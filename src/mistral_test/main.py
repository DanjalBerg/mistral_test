import os
import sys

from mistralai.client import Mistral

MODEL = "mistral-small-latest"


def main() -> None:
    api_key = os.environ.get("MISTRAL_API_KEY")
    if not api_key:
        sys.exit(
            "MISTRAL_API_KEY is not set. "
            'Set it in your terminal first, e.g. export MISTRAL_API_KEY="your-key"'
        )

    client = Mistral(api_key=api_key)

    response = client.chat.complete(
        model=MODEL,
        messages=[
            {"role": "user", "content": "What is the best French cheese?"},
        ],
    )

    print(response.choices[0].message.content)


if __name__ == "__main__":
    main()
