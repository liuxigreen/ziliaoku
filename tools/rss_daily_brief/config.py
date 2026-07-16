# RSS 信源配置 + 评分参数
# ============================================

# 信源列表：名称 -> RSS URL
FEEDS = {
    # --- 聚合器 ---
    "Hacker News": "https://news.ycombinator.com/rss",

    # --- Reddit AI 相关 ---
    "Reddit r/LocalLLaMA": "https://www.reddit.com/r/LocalLLaMA/.rss",
    "Reddit r/MachineLearning": "https://www.reddit.com/r/MachineLearning/.rss",
    "Reddit r/OpenAI": "https://www.reddit.com/r/OpenAI/.rss",
    "Reddit r/singularity": "https://www.reddit.com/r/singularity/.rss",
    "Reddit r/artificial": "https://www.reddit.com/r/artificial/.rss",
    "Reddit r/AgentAI": "https://www.reddit.com/r/AgentAI/.rss",

    # --- 科技媒体 AI 板块 ---
    "The Verge AI": "https://www.theverge.com/rss/ai-artificial-intelligence/index.xml",
    "TechCrunch AI": "https://techcrunch.com/category/artificial-intelligence/feed/",
    "VentureBeat AI": "https://venturebeat.com/category/ai/feed/",

    # --- AI 专业博客 ---
    "AI News": "https://www.artificialintelligence-news.com/feed/",
    "MarkTechPost AI": "https://www.marktechpost.com/category/technology/artificial-intelligence/feed/",

    # --- 开发者工具 ---
    "GitHub Trending (Python)": "https://mshibanami.github.io/GitHubTrendingRSS/daily/python.xml",
    "GitHub Trending (TS)": "https://mshibanami.github.io/GitHubTrendingRSS/daily/typescript.xml",
}

# 来源权重（越高越优先）
SOURCE_WEIGHTS = {
    "Hacker News": 1.5,
    "Reddit r/LocalLLaMA": 1.4,
    "Reddit r/MachineLearning": 1.3,
    "Reddit r/OpenAI": 1.2,
    "Reddit r/singularity": 1.1,
    "Reddit r/AgentAI": 1.2,
    "GitHub Trending (Python)": 1.3,
    "GitHub Trending (TS)": 1.2,
}

# 关键词匹配表（小写）——命中加分
KEYWORDS = [
    # AI/LLM 核心
    "ai", "artificial intelligence", "llm", "large language model",
    "gpt", "chatgpt", "claude", "gemini", "llama", "mistral",
    "openai", "anthropic", "deepmind", "hugging face",
    # 技术
    "agent", "rag", "rag", "fine-tune", "fine-tuning", "fine tune",
    "embedding", "vector", "prompt", "prompting",
    "open source", "open-source", "opensource",
    "model", "training", "inference", "deployment",
    # 工具/工作流
    "tool", "workflow", "automation", "no-code", "low-code",
    "api", "sdk", "framework", "library", "plugin",
    "copilot", "cursor", "vscode", "ide",
    # 开发者
    "developer", "productivity", "coding", "programming",
    "python", "typescript", "javascript", "rust", "go ",
    # 趋势
    "breakthrough", "benchmark", "release", "launch", "update",
]

# 抓取时间窗口（小时）
LOOKBACK_HOURS = 36

# Top N 展示数量
TOP_N = 8

# 请求超时（秒）
REQUEST_TIMEOUT = 20

# User-Agent（部分 RSS 拒绝默认 UA）
USER_AGENT = "Mozilla/5.0 (compatible; RSS-Daily-Brief/1.0; +https://github.com/liuxigreen/ziliaoku)"

# 每个信源之间的礼貌间隔（秒）。
# 拉大间隔 = 请求节奏更温和，不容易瞬时触发限流（Reddit 等连发子版尤其受益）。
# 代价是每日总运行时间变长（14 源 × 间隔，GitHub Actions 免费额度完全够）。
# 本地测试可用环境变量覆盖：RSS_FETCH_INTERVAL=0 跳过全部延迟。
FETCH_INTERVAL_SEC = 3
