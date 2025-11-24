# my money tracker thing
# because apparently my cash evaporates??

stuff_i_bought = []


def main():
    print("hey")
    print("welcome to my extremely serious money tracker\n")

    while True:
        print("what now?")
        print("1) add thing")
        print("2) delete thing")
        print("3) show everything")
        print("4) total spent")
        print("5) leave")

        choice = input("> ").strip()

        if choice == "1":
            add_thing()
        elif choice == "2":
            delete_thing()
        elif choice == "3":
            show_all()
        elif choice == "4":
            show_total()
        elif choice == "5":
            print("bye bye")
            break
        else:
            print("bro just pick 1-5\n")


def add_thing():
    print("\nadding a thing...")

    d = input("when did this happen? ")
    w = input("what did you buy? ")
    m = get_money()

    entry = {"date": d, "what": w, "money": m}
    stuff_i_bought.append(entry)

    print(f"ok added {w} (${m:.2f})\n")


def get_money():
    while True:
        raw = input("how much $$? ")

        try:
            num = float(raw)
        except:
            print("numbers dude. like 12.99")
            continue

        if num <= 0:
            print("it can't be zero or negative lol")
            continue

        return num


def delete_thing():
    if not stuff_i_bought:
        print("nothing to delete\n")
        return

    show_all()

    try:
        n = int(input("which one to delete? "))
    except:
        print("that's not a number\n")
        return

    if n < 1 or n > len(stuff_i_bought):
        print("out of range, try again\n")
        return

    gone = stuff_i_bought.pop(n - 1)
    print(f"deleted {gone['what']}\n")


def show_all():
    if not stuff_i_bought:
        print("literally empty\n")
        return

    print("\nhere's all the damage:")
    total = 0

    for i, t in enumerate(stuff_i_bought, start=1):
        print(f"{i}. {t['date']} - {t['what']} - ${t['money']:.2f}")
        total += t["money"]

    print(f"running total: ${total:.2f}\n")


def show_total():
    if not stuff_i_bought:
        print("you spent: $0 (wow)\n")
        return

    total = sum(t["money"] for t in stuff_i_bought)
    print(f"total spent so far: ${total:.2f}\n")


if __name__ == "__main__":
    main()