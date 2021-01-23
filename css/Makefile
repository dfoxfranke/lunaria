LIGHT_THEME=../lunaria-light.json
DARK_THEME=../lunaria-dark.json
ECLIPSE_THEME=../lunaria-eclipse.json

lunaria.css: gencss.py $(LIGHT_THEME) $(DARK_THEME) $(ECLIPSE_THEME)
	python3 gencss.py > lunaria.css

clean:
	$(RM) lunaria.css

.PHONY: clean