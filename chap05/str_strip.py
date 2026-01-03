msg = " 　こんにちは \t\n\r"

print(f"「{msg.strip()}」")
print(f"「{msg.lstrip()}」")
print(f"「{msg.rstrip()}」")

msg2 = "!====== [独習Python] ======!"
print(f"「{msg2.strip('!= []')}」")
