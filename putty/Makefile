LUNARIZE=python3 ../lunarize.py
LIGHT_THEME=../lunaria-light.json
DARK_THEME=../lunaria-dark.json
ECLIPSE_THEME=../lunaria-eclipse.json

all: lunaria-light.reg lunaria-dark.reg lunaria-eclipse.reg
clean: 
	$(RM) lunaria-light.reg lunaria-dark.reg lunaria-eclipse.reg

lunaria-light.reg: template.reg $(LIGHT_THEME)
	$(LUNARIZE) --format=decimal_rgb $(LIGHT_THEME) $< $@

lunaria-dark.reg: template.reg $(DARK_THEME)
	$(LUNARIZE) --format=decimal_rgb $(DARK_THEME) $< $@

lunaria-eclipse.reg: template.reg $(ECLIPSE_THEME)
	$(LUNARIZE) --format=decimal_rgb $(ECLIPSE_THEME) $< $@

.PHONY: all clean
