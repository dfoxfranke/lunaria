LUNARIZE=python3 ../lunarize.py
LIGHT_THEME=../lunaria-light.json
DARK_THEME=../lunaria-dark.json
ECLIPSE_THEME=../lunaria-eclipse.json

all: light.txt dark.txt eclipse.txt
clean: 
	$(RM) light.txt dark.txt eclipse.txt

light.txt: template.txt $(LIGHT_THEME)
	$(LUNARIZE) $(LIGHT_THEME) $< $@

dark.txt: template.txt $(DARK_THEME)
	$(LUNARIZE) $(DARK_THEME) $< $@

eclipse.txt: template.txt $(ECLIPSE_THEME)
	$(LUNARIZE) $(ECLIPSE_THEME) $< $@

.PHONY: all clean
