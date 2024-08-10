import os

from jinja2 import Template

if __name__ == "__main__":
    os.makedirs("invitations",exist_ok=True)
    template = Template(open('index.html').read())
    guests = (
        ("Роман", "Арина"),
        ("Александр", "Елена"),
        ("Сергей", "ирина"),
        ("Антон", "Дарья"),
        ("Анна", "Алексей"),
        ("Татьяна"),
        ("Полина"),
        ("Жанна"),
        ("Дмитрий", "Юлия"),
        ("Екатерина", "Игорь"),
        ("Наталья", "Дмитрий"),
        ("Елизавета"),
        ("Ксения"),
        ("Ксения"),
        ("Павел"),
        ("Анастасия", "Андрей")

    )
    for guest in guests:
        if len(guest) != 2:
            continue
        guest_1, guest_2 = guest
        with open(f"invitations/{guest_1}_{guest_2}.html", "w") as f:
            rendered_template = template.render(guest_name_1=guest_1, guest_name_2=guest_2)
            f.write(rendered_template)