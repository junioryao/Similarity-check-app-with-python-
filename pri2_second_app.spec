# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['pri2_second_app.py'],
             pathex=['C:\\Users\\junio\\Desktop\\pri2'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=True)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          [('v', None, 'OPTION')],
          exclude_binaries=True,
          name='pri2_second_app',
          debug=True,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=True )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               upx_exclude=[],
               name='pri2_second_app')
