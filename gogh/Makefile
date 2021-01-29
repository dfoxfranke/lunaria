LUNARIZE=python3 ../lunarize.py
LIGHT_THEME=../lunaria-light.json
DARK_THEME=../lunaria-dark.json
ECLIPSE_THEME=../lunaria-eclipse.json

all: lunaria-light.sh lunaria-dark.sh lunaria-eclipse.sh
clean: 
	$(RM) lunaria-light.sh lunaria-dark.sh lunaria-eclipse.sh

lunaria-light.sh: template.sh $(LIGHT_THEME)
	$(LUNARIZE) --format=css_hex $(LIGHT_THEME) $< $@

lunaria-dark.sh: template.sh $(DARK_THEME)
	$(LUNARIZE) --format=css_hex $(DARK_THEME) $< $@

lunaria-eclipse.sh: template.sh $(ECLIPSE_THEME)
	$(LUNARIZE) --format=css_hex $(ECLIPSE_THEME) $< $@

.PHONY: all clean