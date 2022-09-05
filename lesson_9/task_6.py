text = """Любіть Україну, як сонце любіть,
як вітер, і трави, і води...
В годину щасливу і в радості мить,
любіть у годину негоди.

Любіть Україну у сні й наяву,
вишневу свою Україну,
красу її, вічно живу і нову,
і мову її солов'їну.

Без неї — ніщо ми, як порох і дим,
розвіяний в полі вітрами...
Любіть Україну всім серцем своїм
і всіми своїми ділами."""


text1 = text.replace(",", "").replace("—", "").replace(".", "")
txt = dict.fromkeys(text1.split(), 0)

ltxt = text1.split()

most_common = None
qty_most_common = 0


for i in txt:
    txt[i] = ltxt.count(i)
    qty = ltxt.count(i)
    if qty > qty_most_common:
        qty_most_common = qty
        most_common = i

print(txt)
print("Найчастіше зустрічаєтся слово -", most_common, "-", txt[most_common], "разів!")

