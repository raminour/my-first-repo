import requests
import json
from datetime import datetime

def fetch_top_news():
    top_stories_url = "https://hacker-news.firebaseio.com/v0/topstories.json"
    response = requests.get(top_stories_url)
    story_ids = response.json()[:50]

    keywords = ["AI", "OpenAI", "Anthropic", "Google", "Meta", "xAI", "DeepSeek", "Qwen", "MiniMax", "Higgsfield", "Kling", "Runway", "LLM", "Video", "Agent"]
    
    filtered_news = []

    for story_id in story_ids:
        story_url = f"https://hacker-news.firebaseio.com/v0/item/{story_id}.json"
        story_data = requests.get(story_url).json()
        
        if story_data and 'title' in story_data:
            title = story_data['title']
            if any(keyword.lower() in title.lower() for keyword in keywords):
                filtered_news.append({
                    "title": title,
                    "url": story_data.get('url', f"https://news.ycombinator.com/item?id={story_id}")
                })
        
        if len(filtered_news) >= 10:
            break

    if filtered_news:
        today_date = datetime.now().strftime("%Y-%m-%d")
        filename = f"news_{today_date}.md"
        
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(f"# أخبار الذكاء الاصطناعي ليوم {today_date}\n\n")
            for news in filtered_news:
                f.write(f"### {news['title']}\n")
                f.write(f"[اقرأ المصدر]({news['url']})\n\n")
        
        print(f"تم حفظ التقرير بنجاح في ملف {filename}")
    else:
        print("لم يتم العثور على أخبار مطابقة اليوم.")

if __name__ == "__main__":
    fetch_top_news()
