# Get Searched Reply

[English](README.md) | 简体中文

这是一个 CLI Skill 项目，封装了阿里云百炼的模型侧搜索能力。方便 Agent 通过 `search 'query'` 获取 AI 搜索总结。

## 功能特点

- **联网搜索**：利用大模型（如 Qwen-plus）的联网搜索能力获取最新信息。
- **配置驱动**：通过 `config.yaml` 管理 API Key、System Prompt 和模型参数。
- **CLI 集成**：支持作为命令行工具安装，方便 Agent 调用。

## 安装

使用 `uv` 进行可编辑模式安装：

```bash
uv tool install -e .
```

## 配置

在项目根目录下创建 `config.yaml`（可参考 `example.config.yaml`）：

```yaml
api_key: "your_api_key_here"
system_prompt: "You are a helpful assistant."
model: "qwen-plus"
base_url: "https://dashscope.aliyuncs.com/compatible-mode/v1"
```

## 使用方法

### Agent 调用示例

Agent 可以通过执行以下命令来获取搜索总结：

```bash
search "中国队在巴黎奥运会获得了多少枚金牌"
```

### Python 调用

```python
from main import get_reply

reply = get_reply("你的问题")
print(reply)
```
