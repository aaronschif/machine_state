import virtualenv

output = virtualenv.create_bootstrap_script("""
import os, subprocess
def after_install(options, home_dir):
    etc = join(home_dir, 'etc')
    if not os.path.exists(etc):
        os.makedirs(etc)
    # subprocess.call([join(home_dir, 'bin', 'easy_install'), 'pip'])
    subprocess.call([join(home_dir, 'bin', 'pip'), 'install', '-r', 'requirements.pip'])

    print
    print 'Run this:'
    print '========='
    print 'source '+join(home_dir, 'bin', 'activate')+'; ansible-playbook -i hosts machine.yml -K'
""")

with open('bootstrap.out.py', 'w') as f:
    f.write(output)
