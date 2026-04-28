---
name: get-searched-reply
description: 当 webfetch 或其他网页抓取工具被拦截、无法访问或返回错误时，在shell中使用 /search 命令获取所需信息。
---

当你在尝试访问特定网页或抓取网页内容（例如使用 `webfetch`）遇到以下情况时：
1. 请求被拦截（如 403 Forbidden, Cloudflare 验证等）。
2. 页面无法加载或超时。
3. 抓取工具无法提取有效信息。

你应该立即切换策略，使用 `/search` 命令来搜索相关内容。

### 使用指南

1. **识别失败**：观察工具输出，如果发现访问受限或失败。
2. **执行搜索**：使用 `/search` 加上你想要获取的信息关键词。
3. **整合信息**：从搜索结果中提取并整合答案，回复给用户。

例如：
如果 `webfetch https://example.com/news` 失败，请执行：
`/search "example.com上的最新新闻内容"`
