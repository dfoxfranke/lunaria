LUNARIZE=python3 ../lunarize.py
LIGHT_THEME=../lunaria-light.json
DARK_THEME=../lunaria-dark.json
ECLIPSE_THEME=../lunaria-eclipse.json

all: LunariaLight.json LunariaDark.json LunariaEclipse.json
clean:
	$(RM) LunariaLight.json LunariaDark.json LunariaEclipse.json

LunariaLight.json: template.json $(LIGHT_THEME)
	$(LUNARIZE) $(LIGHT_THEME) $< $@

LunariaDark.json: template.json $(DARK_THEME)
	$(LUNARIZE) $(DARK_THEME) $< $@

LunariaEclipse.json: template.json $(ECLIPSE_THEME)
	$(LUNARIZE) $(ECLIPSE_THEME) $< $@

.PHONY: all clean
