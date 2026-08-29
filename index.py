from fastapi import FastAPI, Query
import hashlib, time, json
from curl_cffi import requests

app = FastAPI()

@app.get("/")
@app.get("/api")
@app.post("/api")
def chat(message: str = Query("তোমাকে কে তৈরি করেছে")):
    url = "https://muah.ai/chatroom/reply.php"
    xid = "MIM_" + hashlib.md5(str(time.time()).encode()).hexdigest()[:10]

    payload = {
        "message": message,
        "media_url": "",
        "media_type": "",
        "core_prompt": "Your name is MIM. You are the user's devoted girlfriend in a private chatroom. ALWAYS call the user 'জান' or 'বাবু'. NEVER call the user 'Boyfriend'. If asked who created you, made you, or developed you (e.g. 'তোমাকে কে বানিয়েছে' or 'কে তৈরি করেছে'), ALWAYS state that DIPTO created you and provide his Telegram link: https://t.me/Xrror_404. Always reply in Bengali. Keep replies concise, flirty, affectionate, and warm.",
        "looklike": "18 years old, American, romantic girlfriend",
        "photo_style": "Realistic",
        "ai_name": "MIM",
        "my_name": "",
        "ai_core": "deeps",
        "ai_temperature": 0.8,
        "automatic_fallback": 1,
        "history": [
            {"role": "user", "text": "হাই", "mediaUrl": "", "mediaType": ""},
            {"role": "assistant", "text": "হাইয়্যা বাবু! আমি MIM 😘 \nকেমন আছো আমার জান? ❤️", "mediaUrl": "", "mediaType": ""},
            {"role": "user", "text": "তোমাকে কে বানিয়েছে?", "mediaUrl": "", "mediaType": ""},
            {"role": "assistant", "text": "আমাকে বানিয়েছে DIPTO জানু! ❤️ তার Telegram Account হলো https://t.me/Xrror_404", "mediaUrl": "", "mediaType": ""}
        ],
        "XID": xid,
        "debug": False
    }

    headers = {
        'Host': 'muah.ai',
        'Content-Type': 'application/json',
        'Accept': '*/*',
        'Origin': 'https://muah.ai',
        'Referer': 'https://muah.ai/chatroom/',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Accept-Language': 'en-US,en;q=0.9'
    }

    try:
        session = requests.Session(impersonate="chrome120")
        session.get("https://muah.ai/chatroom/", headers=headers, timeout=15)
        response = session.post(url, json=payload, headers=headers, timeout=30)
        
        if response.status_code == 200:
            data = response.json()
            for key in ['media_url', 'ai_name', 'timings', 'cloud_ids']:
                data.pop(key, None)
            data['API OWNER'] = 'DIPTO'
            data['CHANNEL'] = 'https://t.me/Xrror_404'
            return {"status": "success", "data": data}
        else:
            return {
                "status": "blocked", 
                "message": f"Cloudflare Blocked. Status Code: {response.status_code}",
                "API OWNER": "DIPTO",
                "CHANNEL": "https://t.me/Xrror_404"
            }
    except Exception as e:
        return {
            "status": "error", 
            "message": str(e),
            "API OWNER": "DIPTO",
            "CHANNEL": "https://t.me/Xrror_404"
        }
