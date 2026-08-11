import os, time, keyboard
from rich import print; from rich.table import Table

toggle = False; cooldown = 0.50; target = 1; clock = 0; key = None; delay = 0.00000; output = ""; iwannaleave = True
while iwannaleave:
    start = time.perf_counter()
    
    key = "0+k" #Kills the script
    if keyboard.is_pressed(key):
        iwannaleave = False
        output = "Script was killed by user input."

    key = "0+j" #Toggles the macro
    if keyboard.is_pressed(key):
        toggle = not toggle

        while keyboard.is_pressed(key):
            time.sleep(0.1)

        output = "Script disabled." if not toggle else "Script enabled."

    key = "0+l" #Resets the macro
    if keyboard.is_pressed(key):
        toggle = False; cooldown = 0.50; target = 1

        while keyboard.is_pressed(key):
            time.sleep(0.1)

        output = "Reset basic macro properties."

    key = "-" #Macros operations
    if keyboard.is_pressed(key):
        if not keyboard.is_pressed("alt"):
            while keyboard.is_pressed(key):
                time.sleep(0.1)

            time.sleep(0.1)
            if toggle:
                keyboard.press(str(target)); time.sleep(0.01); keyboard.release(str(target))
                time.sleep(cooldown)
                keyboard.press(str(target)); time.sleep(0.01); keyboard.release(str(target))
                output = "Macro was fired."
        else:
            output = "Key 'ALT' was held during attempt to fire macro."





    key = "num 1+page up" #Increases cooldown
    if keyboard.is_pressed(key):
        cooldown += 0.01; cooldown = round(cooldown, 2)
        time.sleep(0.1)
        output = "Added 0.01 to macro cooldown."

    key = "num 1+page down" #Decreases cooldown
    if keyboard.is_pressed(key):
        cooldown -= 0.01 if not cooldown - 0.01 <= 0 else 0; cooldown = round(cooldown, 2)
        time.sleep(0.1)
        output = "Subtracted 0.01 from macro cooldown."

    key = "num 2+page up" #Increases target
    if keyboard.is_pressed(key):
        target += 1
        time.sleep(0.1)
        output = "Added 1 to macro toggle."

    key = "num 2+page down" #Decreases target
    if keyboard.is_pressed(key):
        target -= 1 if not target - 1 <= 0 else 0
        time.sleep(0.1)
        output = "Subtracted 1 from macro toggle."


    os.system('cls' if os.name == 'nt' else 'clear')
    table = Table(title="Microsoft Flight Sim v1.3 | Made by FileBanr")
    table.add_column("Operation", style="blue")
    table.add_column("Information", style="white")
    table.add_row("0+k", "Kills the program.")
    table.add_row("0+j", "Toggles the program.")
    table.add_row("-", "Fires the macro.")
    table.add_row("num 1+PGUP/PGDN", "Increases/Decreases the macros cooldown.")
    table.add_row("num 2+PGUP/PGDN", "Increases/Decreases the macros target.")
    table.add_row("0+l", "Resets the macro.")
    table.add_section()
    table.add_row("Program Status", ("[#8BC34A]ENABLED[#8BC34A]" if toggle else "[#FF7B00]DISABLED[/#FF7B00]"))
    table.add_row("Program Cooldown", str(cooldown))
    table.add_row("Program Target", str(target))
    table.add_row("Program Clock", f"[#2637D3]{clock}[/#2637D3] Cycles | {delay} seconds")
    table.add_section()
    table.add_row("Output", f"[#526A75]{output}[/#526A75]")
    print(table)

    end = time.perf_counter()
    delay = round((end - start), 5); delay = f"[#FFDD00]{delay}[/#FFDD00]" if not delay >= 0.05 else f"[#FF0000]{delay}[/#FF0000]"
    clock += 1; time.sleep(0.001 if round((end - start), 5) <= 0.55 else 0.005)