LUNARIZE=python3 ../lunarize.py
LIGHT_THEME=../lunaria-light.json
DARK_THEME=../lunaria-dark.json
ECLIPSE_THEME=../lunaria-eclipse.json

all: light.tmTheme dark.tmTheme eclipse.tmTheme
clean:
	$(RM) light.tmTheme dark.tmTheme eclipse.tmTheme

light.tmTheme: template.tmTheme $(LIGHT_THEME)
	$(LUNARIZE) $(LIGHT_THEME) $< $@

dark.tmTheme: template.tmTheme $(DARK_THEME)
	$(LUNARIZE) $(DARK_THEME) $< $@

eclipse.tmTheme: template.tmTheme $(ECLIPSE_THEME)
	$(LUNARIZE) $(ECLIPSE_THEME) $< $@

.PHONY: all clean
