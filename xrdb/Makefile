LUNARIZE=python3 ../lunarize.py
LIGHT_THEME=../lunaria-light.json
DARK_THEME=../lunaria-dark.json
ECLIPSE_THEME=../lunaria-eclipse.json

all: light.xrdb dark.xrdb eclipse.xrdb
clean: 
	$(RM) light.xrdb dark.xrdb eclipse.xrdb

light.xrdb: template.xrdb $(LIGHT_THEME)
	$(LUNARIZE) $(LIGHT_THEME) $< $@

dark.xrdb: template.xrdb $(DARK_THEME)
	$(LUNARIZE) $(DARK_THEME) $< $@

eclipse.xrdb: template.xrdb $(ECLIPSE_THEME)
	$(LUNARIZE) $(ECLIPSE_THEME) $< $@

.PHONY: all clean