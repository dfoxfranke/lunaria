LUNARIZE=python3 ../lunarize.py
LIGHT_THEME=../lunaria-light.json
DARK_THEME=../lunaria-dark.json
ECLIPSE_THEME=../lunaria-eclipse.json

all: LunariaLight.colorscheme LunariaDark.colorscheme LunariaEclipse.colorscheme
clean: 
	$(RM) LunariaLight.colorscheme LunariaDark.colorscheme

LunariaLight.colorscheme: template.colorscheme $(LIGHT_THEME)
	$(LUNARIZE) --format=decimal_rgb $(LIGHT_THEME) $< $@

LunariaDark.colorscheme: template.colorscheme $(DARK_THEME)
	$(LUNARIZE) --format=decimal_rgb $(DARK_THEME) $< $@

LunariaEclipse.colorscheme: template.colorscheme $(ECLIPSE_THEME)
	$(LUNARIZE) --format=decimal_rgb $(ECLIPSE_THEME) $< $@

.PHONY: all clean