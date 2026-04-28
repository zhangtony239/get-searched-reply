import yaml
from openai import OpenAI

def get_reply(prompt: str) -> str:
    # 从 config.yaml 读取配置
    with open("config.yaml", "r", encoding="utf-8") as f:
        config = yaml.safe_load(f)
    
    api_key = config.get("api_key")
    system_prompt = config.get("system_prompt", "You are a helpful assistant.")
    model = config.get("model", "deepseek-v4-flash")
    base_url = config.get("base_url", "https://dashscope.aliyuncs.com/compatible-mode/v1")

    client = OpenAI(
        api_key=api_key,
        base_url=base_url,
    )

    completion = client.chat.completions.create(
        model=model,
        messages=[
            {'role': 'system', 'content': system_prompt},
            {'role': 'user', 'content': prompt}
        ],
        extra_body={
            "enable_search": True
        }
    )
    
    content = completion.choices[0].message.content
    return content if content is not None else ""

if __name__ == "__main__":
    # 示例调用
    try:
        reply = get_reply("中国队在巴黎奥运会获得了多少枚金牌")
        print(reply)
    except Exception as e:
        print(f"Error: {e}")
