# https://docs.google.com/document/d/19SqDIlDkcl4NZreH-IZ
# -0FNYEb5RQef1BFiZRZGN4LA/edit?usp=sharing
# 🐿 🐮 🐭 🐫 🐯 🦏 🦍 🦊 🦒 🐀 🐨 🦘 🐖 🦇 🦓 🐰 🦝 🦔 🦄 🐆 🐄 🐷 🦙 🐽 🦁 🐻 🐈 🐣 🐔
# 🐤 🦜 🐧 🦉 🦃 🦚 🐸 🐍 🦎
# 🐊 🦖 🐲 🐉 🐋 🦈 🐳 🐙 🦋 🦠 🦂 🕷 🐜 🌹 🌺 🌼 🌻 🌴 🌲 🌳 🍂 ☘ 🌈 🐕
#  ▖ ▗ ▘ ▙ ▚ ▛ ▜ ▝ ▞ ▟ ■ □ ▢ ▣ ▤ ▥ ▦ ▧ ▨ ▩ ▪ ▫ ▬ ▭ ▮ ▯ ▰ ▱ ▲ △ ▴ ▵ ▶ ▷ ▸ ▹ ► ▻
#  ▼ ▽ ▾ ▿ ◀ ◁ ◂ ◃ ◄ ◅ ◆ ◇ ◈ ◉ ◊ ○ ◌ ◍ ◎ ● ◐
#  ◑ ◒ ◓ ◔ ◕ ◖ ◗ ◘ ◙ ◚ ◛ ◜ ◝ ◞ ◟ ◠ ◡ ◢ ◣ ◤ ◥ ◦ ◧ ◨ ◩ ◪ ◫ ◬ ◭ ◮ ◯ ◰ ◱ ◲ ◳ ◴ ◵ ◶ ◷
#  ◸ ◹ ◺ ◻ ◼ ◽ ◾ ◿
# ① ② ③ ④ ⑤ ⑥ ⑦ ⑧ ⑨ ⑩ ⑪ ⑫ ⑬ ⑭ ⑮ ⑯ ⑰ ⑱ ⑲ ⑳ ⑴ ⑵ ⑶ ⑷ ⑸ ⑹ ⑺ ⑻ ⑼
# ⑽ ⑾ ⑿ ⒀ ⒁ ⒂ ⒃ ⒄ ⒅ ⒆ ⒇ ⒈ ⒉ ⒊ ⒋ ⒌ ⒍ ⒎ ⒏ ⒐ ⒑ ⒒ ⒓ ⒔ ⒕ ⒖ ⒗ ⒘ ⒙
# ⒚ ⒛ ⒜ ⒝ ⒞ ⒟ ⒠ ⒡ ⒢ ⒣ ⒤ ⒥ ⒦ ⒧ ⒨ ⒩ ⒪ ⒫ ⒬ ⒭ ⒮ ⒯ ⒰ ⒱ ⒲ ⒳ ⒴ ⒵
# Ⓐ Ⓑ Ⓒ Ⓓ Ⓔ Ⓕ Ⓖ Ⓗ Ⓘ Ⓙ Ⓚ Ⓛ Ⓜ Ⓝ Ⓞ Ⓟ Ⓠ Ⓡ Ⓢ Ⓣ Ⓤ Ⓥ Ⓦ Ⓧ Ⓨ Ⓩ ⓐ ⓑ ⓒ
# ⓓ ⓔ ⓕ ⓖ ⓗ ⓘ ⓙ ⓚ ⓛ ⓜ ⓝ ⓞ ⓟ ⓠ ⓡ ⓢ ⓣ ⓤ ⓥ ⓦ ⓧ ⓨ ⓩ ⓪
# ⓿ ❶ ❷ ❸ ❹ ❺ ❻ ❼ ❽ ❾ ❿ ⓫ ⓬ ⓭ ⓮ ⓯ ⓰ ⓱ ⓲ ⓳ ⓴


directive = "\033["
colour = {
    "black": "30m",
    "red": "31m",
    "green": "32m",
    "yellow": "33m",
    "blue": "34m",
    "purple": "35m",
    "turquoise": "36m",
    "white": "37m"
}

background = {
    "black": "40m",
    "red": "41m",
    "green": "42m",
    "yellow": "43m",
    "blue": "44m",
    "purple": "45m",
    "turquoise": "45m",
    "white": "47m"
}


style = {
    "clean": "0m",
    "italics": "3m",
    "grey": "2m",
    "bold": "1m",
    "underlined": "4m",
    "slow_flash": "5m",
    "fast_flash": "6m",
    "blink": "7m",
}


def color_format(
    text: str,
    styled: str = "italics", fg: str = "blue", bg: str = "black",
    no_bg: bool = False
) -> str:
    styled_text = directive + style[styled]
    fg_text = directive + colour[fg]
    bg_text = directive + background[bg]
    clean_code = directive + style['clean']
    return \
        styled_text + fg_text + bg_text + text + \
        clean_code if no_bg else styled_text +\
        fg_text + text + clean_code


if __name__ == "__main__":
    print(color_format("This is default blue text"))
    print(color_format("This is red text", fg="red"))
    print(color_format("▓", fg="white"))