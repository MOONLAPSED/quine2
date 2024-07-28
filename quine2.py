'{source_code}\n\ndef git_pull():\n    result = subprocess.run([\'git\', \'pull\'], capture_output=True, text=True)\n    return result.returncode == 0 and \'Already up to date\' not in result.stdout\n\ndef git_commit():\n    with open(__file__, \'w\') as f:\n        # Write the quine script, including this function and below lines\n        f.write(quine_template.format(source_code=repr(quine_template)))\n    subprocess.run([\'git\', \'add\', __file__])\n    subprocess.run([\'git\', \'commit\', \'-m\', \'Update quine at runtime\'])\n    subprocess.run([\'git\', \'push\'])\n\ndef quine():\n    if git_pull():\n        os.execv(sys.executable, [\'python\'] + sys.argv)\n    else:\n        print(quine_template.format(source_code=repr(quine_template)))\n        git_commit()\n\nif __name__ == "__main__":\n    quine()\n'

def git_pull():
    result = subprocess.run(['git', 'pull'], capture_output=True, text=True)
    return result.returncode == 0 and 'Already up to date' not in result.stdout

def git_commit():
    with open(__file__, 'w') as f:
        # Write the quine script, including this function and below lines
        f.write(quine_template.format(source_code=repr(quine_template)))
    subprocess.run(['git', 'add', __file__])
    subprocess.run(['git', 'commit', '-m', 'Update quine at runtime'])
    subprocess.run(['git', 'push'])

def quine():
    if git_pull():
        os.execv(sys.executable, ['python'] + sys.argv)
    else:
        print(quine_template.format(source_code=repr(quine_template)))
        git_commit()

if __name__ == "__main__":
    quine()
