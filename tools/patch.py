"""Turn a copy of the seattlesinner site into the Seattle Edition mirror.
Only the masthead and this site's own settings change; all content stays identical."""
import re, sys, os, shutil
site, overlay = sys.argv[1], sys.argv[2]
shutil.copytree(overlay, site, dirs_exist_ok=True)
domain = os.environ.get('MIRROR_DOMAIN', '').strip()
if domain:
    open(os.path.join(site, 'CNAME'), 'w').write(domain + '\n')
elif os.path.exists(os.path.join(site, 'CNAME')):
    os.remove(os.path.join(site, 'CNAME'))
p = os.path.join(site, 'index.html'); h = open(p).read()
h2, n = re.subn(r'<img src="img/masthead\.png[^"]*" alt="[^"]*" width="1440" height="\d+">',
                '<img src="img/masthead-edition.png?v=1" alt="Guitar Doug Report, Seattle Edition" width="1440" height="211">', h)
if n != 1:
    sys.exit('masthead tag not found; mirror not published')
open(p, 'w').write(h2)
for junk in ['.github', '.git']:
    shutil.rmtree(os.path.join(site, junk), ignore_errors=True)
print('patched masthead; domain =', domain or '(none yet)')
