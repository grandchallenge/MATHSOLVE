from pathlib import Path
ROOT=Path(__file__).resolve().parent
snapshot=ROOT/'ProtectedSnapshot-original.lean.txt'
if not snapshot.exists(): snapshot=ROOT/'protected-ThreeUniform.lean'
text=snapshot.read_text(encoding='utf-8')
body=text[text.index('open Cardinal Set'):].rstrip()
assert body.endswith('\nend')
body=body[:-len('\nend')]
license=text[:text.index('module\n')]
out=license+'import RequestProject.PublicationCertificate\n\nnamespace ProtectedSnapshot\n\n'+body+'\n\nend ProtectedSnapshot\n'
(ROOT/'ProtectedInterface.lean').write_text(out,encoding='utf-8',newline='\n')
