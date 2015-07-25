# -*- mode: python -*-
a = Analysis(['src\\main.py'],
             pathex=['src', 'D:\\2015\\July\\VCF'],
             hiddenimports=[],
             hookspath=None,
             runtime_hooks=None)
pyz = PYZ(a.pure)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='main.exe',
          debug=False,
          strip=None,
          upx=True,
          console=False )
