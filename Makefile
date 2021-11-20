TOPTARGETS := all clean
SUBDIRS := css gogh kitty qterminal tmtheme vscode winterminal xrdb

$(TOPTARGETS): $(SUBDIRS)
$(SUBDIRS):
	$(MAKE) -C $@ $(MAKECMDGOALS)

.PHONY: $(TOPTARGETS) $(SUBDIRS)
