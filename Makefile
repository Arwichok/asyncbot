init:
	python3 main.py init
	make compiletext

gettext:
	pybabel extract bot/ -o locales/bot.pot

createtexts:
	echo {en,ru,uk} | xargs -n1 pybabel init -i locales/bot.pot -d locales -D bot -l

updatetext:
	pybabel update -d locales -D bot -i locales/bot.pot

compiletext:
	pybabel compile -d locales -D bot

update:
	make gettext
	make updatetext

build:
	make compiletext