# mistral_test

Minimal Mistral chat completion example using the official Python SDK (`mistralai`).

## 1. Install the SDK

```bash
pip install mistralai
```

or install from the pinned file:

```bash
pip install -r requirements.txt
```

## 2. Generate an API key in Studio

1. Sign in to [Studio](https://console.mistral.ai) (the Mistral developer console).
2. In the left sidebar, open **API keys**.
3. Click **New key**, give it a name (e.g. `mistral_test`) and set an expiration date.
4. Copy the key immediately — it is shown only once and cannot be retrieved later.

## 3. Set `MISTRAL_API_KEY` in your terminal

macOS / Linux (current terminal session):

```bash
export MISTRAL_API_KEY="your-key"
```

To persist it, add the same line to `~/.zshrc` or `~/.bashrc` and run `source ~/.zshrc`.

Windows PowerShell (current session):

```powershell
$env:MISTRAL_API_KEY = "your-key"
```

To persist it on Windows:

```powershell
setx MISTRAL_API_KEY "your-key"
```

## 4. Run the example

From the project folder:

```bash
python main.py
```

The script reads `MISTRAL_API_KEY` from the environment, sends one chat completion
request to `mistral-small-latest`, and prints the assistant's reply.

## GitHub integration (Vibe Code)

If you work on this repository with Vibe Code (Le Chat workflows):

- Vibe Code runs in an ephemeral cloud sandbox and only works with **existing** GitHub
  repositories — it clones the repo into the sandbox, it cannot create one.
- Connect your GitHub account in Le Chat (**Settings → Connectors**) and install the
  Mistral GitHub App: <https://github.com/apps/mistralai/installations/new>
- Give the app access to this repository with **Contents: Read and write** and
  **Pull requests: Read and write**. Without these, pushes fail with `403` and PR
  creation fails with `Resource not accessible by integration`.
- All changes are committed and pushed directly to GitHub (branch + pull request).
  The sandbox is deleted after the session and is not accessible locally.

## Docs

- [Chat completions](https://docs.mistral.ai/studio/conversations/chat-completion)
- [Create your first API key (Studio quickstart)](https://docs.mistral.ai/getting-started/quickstarts/studio/activate-and-generate-api-key)
