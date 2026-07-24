# Урок 18 — Git-ветки и Pull Request

Дата: 2026-07-16
Код: [lesson18.py](../../month1/week4/lesson18.py)
Практика: Pull Request #1.
Статус: полный цикл выполнен; целевая пересдача Git workflow пройдена 2026-07-20.

## Цель

Изолировать изменение от стабильной `main`, опубликовать ветку, провести review
и безопасно вернуть результат в локальную основную ветку.

## Что такое ветка

Ветка — подвижный указатель на коммит, а не отдельная копия папки. Рабочее дерево
общее для текущего checkout, поэтому незакоммиченные изменения могут перейти при
переключении ветки.

## Полный workflow

```powershell
git switch main
git pull
git switch -c feature/name
# изменить и проверить файлы
git status
git add <paths>
git commit -m "describe change"
git push -u origin feature/name
```

На GitHub создаётся Pull Request:

1. посмотреть diff;
2. описать цель и проверку;
3. провести review;
4. исправления оформить новым коммитом и push;
5. выполнить merge.

После merge:

```powershell
git switch main
git pull
git branch -d feature/name
git push origin --delete feature/name
```

Удаление слитой ветки не удаляет её коммиты из истории `main`.

## Состояния и публикация

`working tree -> git add -> staging area -> git commit -> local history -> git push -> remote branch`

Push публикует коммиты. PR организует проверку и слияние. Это разные действия.

## Что было выполнено

- Создана `lesson/git-branches`.
- Выполнены два осмысленных коммита и `push -u`.
- Создан и проверен PR #1.
- Исправлены `week_focus`, длинная строка и trailing whitespace.
- Выполнены merge, pull и удаление веток.

## Ошибки и корректировки

- Ветка сначала воспринималась как новая папка.
- После commit ожидались изменения в `git status`; staging очищается после фиксации.
- Считалось, что после push коммит существует только на GitHub; он остаётся локально.
- На месячном экзамене полный workflow потребовал восстановления и был затем
  воспроизведён с точными командами.

## Math Core

История Git — Directed Acyclic Graph (DAG). `ahead` и `behind` показывают число
коммитов, существующих только в одной из сравниваемых историй.

## English Core

- **branch** — ветка;
- **commit** — коммит;
- **working tree** — рабочее дерево;
- **staging area** — область подготовки;
- **pull request** — запрос на review и слияние;
- **merge** — слияние;
- **upstream** — отслеживаемая ветка;
- **merge conflict** — конфликт слияния.

## Anki

1. **Когда создавать ветку?** — До изменения, которое нужно изолировать от стабильной `main`.
2. **Как изменение проходит до GitHub?** — Working tree → add → staging → commit → local history → push → remote.
3. **Чем push отличается от PR?** — Push публикует коммиты, PR организует проверку и merge.
4. **Что делать локально после merge на GitHub?** — `git switch main`, затем `git pull`.

## Урок усвоен, если

- воспроизводишь workflow без подсказок;
- создаёшь ветку от актуального `main` до изменений;
- различаешь commit, push, PR и merge;
- безопасно обновляешь main и удаляешь слитую ветку.
