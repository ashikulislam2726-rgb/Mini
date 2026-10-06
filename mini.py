#!/data/data/com.termux/files/usr/bin/python3
import getpass, json, time, urllib.error, urllib.request

API_URL = "https://openrouter.ai/api/v1/chat/completions"
PRIMARY_MODEL = "google/gemma-4-26b-a4b-it:free"
FALLBACK_MODEL = "openrouter/free"

SYSTEM_PROMPT = """You are Mini, a fast Termux coding assistant.
Give practical, copy-paste-ready solutions.
When writing code, use complete code blocks and explain where files go.
Prefer Termux-compatible commands and Python standard library when possible.
Never expose or invent API keys."""

def ask(model, key, messages):
    payload = json.dumps({
        "model": model,
        "messages": messages,
        "temperature": 0.2
    }).encode()
    req = urllib.request.Request(
        API_URL,
        data=payload,
        headers={
            "Authorization": "Bearer " + key,
            "Content-Type": "application/json",
            "HTTP-Referer": "https://github.com/ashikulislam2726-rgb/Mini",
            "X-Title": "Mini-Codex"
        },
        method="POST"
    )
    try:
        with urllib.request.urlopen(req, timeout=90) as r:
            data = json.loads(r.read().decode())
        return data["choices"][0]["message"]["content"]
    except urllib.error.HTTPError as e:
        body = e.read().decode(errors="replace")
        raise RuntimeError(f"HTTP {e.code}: {body[:800]}")

def main():
    print("\033[96m╭────────────────────────────────────╮\033[0m")
    print("\033[96m│        MINI • TERMUX AI CODEX      │\033[0m")
    print("\033[96m│   Gemma 4 26B A4B • OpenRouter      │\033[0m")
    print("\033[96m╰────────────────────────────────────╯\033[0m")
    key = getpass.getpass("🔑 Put your OpenRouter API key here: ").strip()
    if not key:
        print("❌ API key is required.")
        return
    messages = [{"role":"system","content":SYSTEM_PROMPT}]
    print("Type 'exit' to quit.\n")
    while True:
        try:
            prompt = input("\033[92mYou › \033[0m").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nBye 👋")
            break
        if prompt.lower() in {"exit","quit","bye"}:
            print("Bye 👋")
            break
        if not prompt:
            continue
        messages.append({"role":"user","content":prompt})
        try:
            try:
                answer = ask(PRIMARY_MODEL, key, messages)
            except RuntimeError as e:
                if any(x in str(e) for x in ("HTTP 429","HTTP 500","HTTP 502","HTTP 503","HTTP 504")):
                    print("⚡ Primary model busy — switching to OpenRouter free routing...")
                    answer = ask(FALLBACK_MODEL, key, messages)
                else:
                    raise
            messages.append({"role":"assistant","content":answer})
            print("\n\033[96mMini ›\033[0m " + answer + "\n")
        except Exception as e:
            if messages and messages[-1]["role"] == "user":
                messages.pop()
            print("❌ Error:", e)
            print("Try again in a moment.\n")

if __name__ == "__main__":
    main()
