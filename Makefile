TOPTARGETS := all clean
SUBDIRS := css qterminal vscode winterminal xrdb gogh

$(TOPTARGETS): $(SUBDIRS)
$(SUBDIRS):
	$(MAKE) -C $@ $(MAKECMDGOALS)

.PHONY: $(TOPTARGETS) $(SUBDIRS)
