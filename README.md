# Get Searched Reply

English | [简体中文](README_zh.md)

This is a CLI Skill project that wraps Alibaba Cloud's model-side search capabilities. It allows Agents to obtain AI-generated search summaries via the `search 'query'` command.

## Features

- **Online Search**: Leverages the web search capabilities of LLMs (e.g., Qwen-plus) to fetch up-to-date information.
- **Configuration Driven**: Easily manage API Key, System Prompt, and model parameters via `config.yaml`.
- **CLI Integration**: Supports installation as a command-line tool for seamless Agent invocation.

## Installation

Install in editable mode using `uv`:

```bash
uv tool install -e .
```

## Configuration

Create a `config.yaml` in the project root (refer to `example.config.yaml`):

```yaml
api_key: "your_api_key_here"
system_prompt: "You are a helpful assistant."
model: "qwen-plus"
base_url: "https://dashscope.aliyuncs.com/compatible-mode/v1"
```

## Usage

### Agent Invocation Example

Agents can execute the following command to get a search summary:

```bash
search "How many gold medals did China win at the Paris Olympics?"
```

### Python Invocation

```python
from main import get_reply

reply = get_reply("Your question")
print(reply)
```
