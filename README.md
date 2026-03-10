# Personal Assistant Bot

CLI-бот для управління контактами та нотатками.

## Структура

```
src/
  models/
    fields.py        — Field, Name, Phone, Birthday, Email, Address
    record.py        — Record (контакт)
    address_book.py  — AddressBook (колекція контактів)
    note.py          — Note, Tag
    notebook.py      — NoteBook (колекція нотаток)
  utils/
    decorators.py    — input_error декоратор
    storage.py       — збереження/завантаження даних (pickle)
    suggest.py       — підказка найближчої команди
  main.py            — точка входу, CLI loop
```

## Запуск

```bash
python -m src.main
```

## Команди

### Контакти
| Команда | Опис |
|---------|------|
| `add <name> <phone>` | Додати контакт |
| `change <name> <old_phone> <new_phone>` | Змінити телефон |
| `phone <name>` | Показати телефони |
| `all` | Показати всі контакти |
| `add-birthday <name> <DD.MM.YYYY>` | Додати день народження |
| `show-birthday <name>` | Показати день народження |
| `birthdays <days>` | Дні народження через N днів |
| `add-email <name> <email>` | Додати email |
| `edit-email <name> <email>` | Змінити email |
| `add-address <name> <address>` | Додати адресу |
| `edit-address <name> <address>` | Змінити адресу |
| `search <query>` | Пошук контактів |
| `delete <name>` | Видалити контакт |

### Нотатки
| Команда | Опис |
|---------|------|
| `add-note <title>` | Додати нотатку |
| `show-notes` | Показати всі нотатки |
| `find-note <query>` | Пошук нотаток |
| `edit-note <id>` | Редагувати нотатку |
| `delete-note <id>` | Видалити нотатку |

### Теги
| Команда | Опис |
|---------|------|
| `add-tag <note_id> <tag>` | Додати тег |
| `remove-tag <note_id> <tag>` | Видалити тег |
| `find-by-tag <tag>` | Пошук за тегом |
| `sort-by-tag` | Сортування за тегами |

### Інше
| Команда | Опис |
|---------|------|
| `hello` | Привітання |
| `help` | Список команд |
| `close` / `exit` | Вихід (автозбереження) |
