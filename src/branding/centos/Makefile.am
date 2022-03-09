centosbrandingdir = $(datadir)/cockpit/branding/centos

dist_centosbranding_DATA = \
	src/branding/centos/branding.css \
	$(NULL)

# Opportunistically use fedora-logos
install-data-hook::
	$(LN_S) -f /usr/share/pixmaps/ablestack/logo.png $(DESTDIR)$(centosbrandingdir)/logo.png
	$(LN_S) -f /usr/share/pixmaps/ablestack/apple-touch-icon.png $(DESTDIR)$(centosbrandingdir)/apple-touch-icon.png
	$(LN_S) -f /usr/share/pixmaps/ablestack/favicon.png $(DESTDIR)$(centosbrandingdir)/favicon.ico
