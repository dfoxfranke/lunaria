LUNARIZE=python3 ../lunarize.py
LIGHT_THEME=../lunaria-light.json
DARK_THEME=../lunaria-dark.json
ECLIPSE_THEME=../lunaria-eclipse.json

all: light.conf dark.conf eclipse.conf
clean:
	$(RM) light.conf dark.conf eclipse.conf

light.conf: template.conf $(LIGHT_THEME)
	$(LUNARIZE) $(LIGHT_THEME) $< $@

dark.conf: template.conf $(DARK_THEME)
	$(LUNARIZE) $(DARK_THEME) $< $@

eclipse.conf: template.conf $(ECLIPSE_THEME)
	$(LUNARIZE) $(ECLIPSE_THEME) $< $@

.PHONY: all clean
