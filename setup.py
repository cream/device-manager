from cream.dist import setup

setup('src/manifest.xml',
    data_files = [
        ('{module_dir}', ['src/manager.py', 'src/manifest.xml'])
        ]
    )
