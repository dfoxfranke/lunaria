LUNARIZE=python3 ../lunarize.py
LIGHT_THEME=../lunaria-light.json
DARK_THEME=../lunaria-dark.json
ECLIPSE_THEME=../lunaria-eclipse.json

all: themes/light.json themes/dark.json themes/eclipse.json
clean: 
	$(RM) themes/light.json themes/dark.json themes/eclipse.json

themes/light.json: themes/template.json $(LIGHT_THEME)
	$(LUNARIZE) $(LIGHT_THEME) $< $@

themes/dark.json: themes/template.json $(DARK_THEME)
	$(LUNARIZE) $(DARK_THEME) $< $@

themes/eclipse.json: themes/template.json $(ECLIPSE_THEME)
	$(LUNARIZE) $(ECLIPSE_THEME) $< $@

.PHONY: all clean