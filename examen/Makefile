

all:
	@echo "Compilación y ejecución de la práctica"

clean:
	@echo "Limpiando..."

git:
	git add *
	git commit -m "$(nm)"
	git push origin master


cli:
	clear
	python3 cli.py

test:
	clear
	python3 -m unittest -v test.py

serv:
	clear
	python3 serv.py
