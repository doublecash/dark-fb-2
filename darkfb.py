# coding: utf-8
import getpass
import time,os,sys

def kntl(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.1)

def tik():
    titik = [
     '.   ', '..  ', '... ']
    for o in titik:
        print '\r\x1b[1;91m[\xe2\x97\x8f] \x1b[1;92mCrack \x1b[1;97m' + o,
        sys.stdout.flush()
        time.sleep(1)

logo = '''
\x1b[1;90m ___    ___
\x1b[1;90m( _<    >_ )           \x1b[1;91m~  ~   \x1b[1;92m┌∩┐\x1b[1;97m(\x1b[1;91m◣_◢\x1b[1;97m)\x1b[1;92m┌∩┐   \x1b[1;91m~  ~
\x1b[1;90m//        \\\   \x1b[1;96m╔═╦══╗╔══╗╔═══╗═╦ ╔══       \x1b[1;92m╔════╗╔══╗
\x1b[1;90m\\\___\x1b[1;91m..\x1b[1;90m___//     \x1b[1;96m║  ║║  ║║   ║ ║ ║         \x1b[1;92m║     ║  ║
\x1b[1;90m `-(    )-'      \x1b[1;96m║  ║╠══╣╠═╦═╝ ╠═╩═╗ \x1b[1;91m«---»\x1b[1;92m ╠══╣  ╠══╩═╗
\x1b[1;90m   _|__|_        \x1b[1;96m║  ║║  ║║ ║   ║   ║       \x1b[1;92m║     ║    ║
\x1b[1;90m  /_|__|_\      \x1b[1;96m═╩══╝╩  ╩╩ ╚══ ╩   ╩       \x1b[1;92m╩     ╚════╝ \x1b[1;93mv2.0
\x1b[1;90m  /_|__|_\     \x1b[1;94m╔════════════════════════════════════════════╗
\x1b[1;90m  /_\__/_\     \x1b[1;94m║\x1b[1;97m{\x1b[1;92m•\x1b[1;97m} \x1b[1;97mAuthor  \x1b[1;91m: \x1b[1;96mSanz                          \x1b[1;94m║
\x1b[1;90m   \ || /  _)  \x1b[1;94m║\x1b[1;97m{\x1b[1;92m•\x1b[1;97m} \x1b[1;97mYoutube \x1b[1;91m: \x1b[1;96mSANZ SOEKAMTI                 \x1b[1;94m║
\x1b[1;90m     ||   ( )  \x1b[1;94m║\x1b[1;97m{\x1b[1;92m•\x1b[1;97m} \x1b[1;97mGithub  \x1b[1;91m: \x1b[1;97m\x1b[4;92mhttps://github.com/B4N954N2-ID\x1b[0m\x1b[1;94m║
\x1b[1;90m     \\\___//   \x1b[1;94m╚════════════════════════════════════════════╝
\x1b[1;90m      `---' '''

os.system('clear')
time.sleep(1)
raw_input('\n\x1b[0;97m[\x1b[0;92m?\x1b[0;97m] Licensi : ')
time.sleep(2)
print '\x1b[1;91m[\x1b[1;96m✓\x1b[1;91m] \x1b[1;92mLicensi Benar'
time.sleep(1)
os.system('clear')
time.sleep(1)
print logo
print '\n\x1b[1;94m╔════════════════════════════════════╗'
print '\x1b[1;94m║      \x1b[1;92mLOGIN AKUN FACEBOOK ANDA      \x1b[1;94m║'
print '\x1b[1;94m╚════════════════════════════════════╝'
id = raw_input('\x1b[1;91m[+] \x1b[1;96mID/Email \x1b[1;91m: \x1b[1;93m')
pwd = getpass.getpass('\x1b[1;91m[+] \x1b[1;96mPassword \x1b[1;91m:\x1b[1;92m ')
kntl('\x1b[1;91m[+] \x1b[1;92mSedang Masuk \x1b[1;97m...')
time.sleep(5)
print '\x1b[1;91m[\x1b[1;96m✓\x1b[1;91m] \x1b[1;92mLogin Berhasil'
os.system('xdg-open https://www.youtube.com/channel/UCqp78GUXAJsSteeJqGu9HBg')
time.sleep(8)
os.system('clear')
time.sleep(1)
print logo
print '\n\x1b[1;94m╔══════════════════════════════════════════════'
print '\x1b[1;94m║ \x1b[1;91m[\x1b[1;92m✓\x1b[1;91m] \x1b[1;97mNama \x1b[1;91m: \x1b[1;93mAkon Tumbal\x1b[1;97m'
print '\x1b[1;94m║ \x1b[1;91m[\x1b[1;92m✓\x1b[1;91m] \x1b[1;97mID   \x1b[1;91m: \x1b[1;93m100025338451765\x1b[1;97m'
print '\x1b[1;94m╚══════════════════════════════════════════════'
print '\x1b[1;97m(\x1b[1;92m1\x1b[1;97m) Informasi Pengguna'
print '(\x1b[1;92m2\x1b[1;97m) Hack Akun Facebook'
print '\x1b[1;97m(\x1b[1;92m3\x1b[1;97m) Lihat Daftar Grup'
print '\x1b[1;97m(\x1b[1;92m4\x1b[1;97m) Ambil ID/Email/No HP'
print '\x1b[1;97m(\x1b[1;92m5\x1b[1;97m) Yahoo clone'
print '\x1b[1;97m(\x1b[1;92m0\x1b[1;97m)\x1b[1;91m Keluar'
pil = raw_input('\n\x1b[1;91m~► \x1b[1;92m')
time.sleep(1)
os.system('clear')
print logo
print '\n'
print 42 * '\x1b[1;94m═'
print '\x1b[1;97m(\x1b[32;1m1\x1b[1;97m) Crack dari daftar teman'
print '\x1b[1;97m(\x1b[32;1m2\x1b[1;97m) Crack dari teman dari teman'
print '\x1b[1;97m(\x1b[32;1m3\x1b[1;97m) Crack dari member grup'
print '\x1b[1;97m(\x1b[32;1m4\x1b[1;97m) Crack dari file'
print '\x1b[1;97m(\x1b[1;91m0\x1b[1;97m)\x1b[1;91m Kembali'
raw_input('\n\x1b[1;91m~► \x1b[1;92m')
os.system('clear')
print logo
print '\n'
print 42 * '\x1b[1;94m═'
raw_input('\x1b[1;91m[+] \x1b[1;92mMasukan ID Teman \x1b[1;91m: \x1b[1;97m')
time.sleep(2)
print '\x1b[1;91m[+] \x1b[1;92mNama Teman \x1b[1;91m: \x1b[1;97mM Riidho'
time.sleep(1)
kntl('\x1b[1;91m[+] \x1b[1;92mMengambil ID \x1b[1;97m...')
time.sleep(2)
print '\x1b[1;91m[+] \x1b[1;92mTotal ID \x1b[1;91m: \x1b[1;97m4.241'
time.sleep(1)
kntl('\x1b[1;91m[+] \x1b[1;92mMembuka Keamanan \x1b[1;97m...')
time.sleep(1)
tik()
kntl('\n\x1b[1;91m[+] \x1b[1;92mStart \x1b[1;97m...')
print '\x1b[1;91m[!] \x1b[1;92mStop CTRL+z'
print 42 * '\x1b[1;94m═'
time.sleep(10)
print '\x1b[1;91m[ \x1b[1;92mOK✓\x1b[1;91m ]  \x1b[1;97m100022297170314  \x1b[1;91m|  \x1b[1;97mSayang'
time.sleep(12)
print '\x1b[1;91m[ \x1b[1;92mOK✓\x1b[1;91m ]  \x1b[1;97m100025059340386  \x1b[1;91m|  \x1b[1;97mDimas123'
time.sleep(10)
print '\x1b[1;91m[ \x1b[1;92mOK✓\x1b[1;91m ]  \x1b[1;97m100028333721788  \x1b[1;91m|  \x1b[1;97mDika12345'
time.sleep(12)
print '\x1b[1;91m[ \x1b[1;93mCP+\x1b[1;91m ]  \x1b[1;97m100028929265579  \x1b[1;91m|  \x1b[1;97mBayu123'
time.sleep(7)
print '\x1b[1;91m[ \x1b[1;92mOK✓\x1b[1;91m ]  \x1b[1;97m100065436809777  \x1b[1;91m|  \x1b[1;97mMusa12345'
time.sleep(9)
print '\x1b[1;91m[ \x1b[1;92mOK✓\x1b[1;91m ]  \x1b[1;97m100021145677888  \x1b[1;91m|  \x1b[1;97mFahmi123'
time.sleep(10)
print '\x1b[1;91m[ \x1b[1;93mCP+\x1b[1;91m ]  \x1b[1;97m100099877882673  \x1b[1;91m|  \x1b[1;97mWahyudi12345'
time.sleep(14)
print '\x1b[1;91m[ \x1b[1;93mCP+\x1b[1;91m ]  \x1b[1;97m100025526727176  \x1b[1;91m|  \x1b[1;97mAdilia123'
time.sleep(10)
print '\x1b[1;91m[ \x1b[1;93mCP+\x1b[1;91m ]  \x1b[1;97m100077265556771  \x1b[1;91m|  \x1b[1;97mFeri123'
time.sleep(8)
print '\x1b[1;91m[ \x1b[1;93mCP+\x1b[1;91m ]  \x1b[1;97m100067865456726  \x1b[1;91m|  \x1b[1;97mBangsat'
time.sleep(11)
print '\x1b[1;91m[ \x1b[1;93mCP+\x1b[1;91m ]  \x1b[1;97m100082765525090  \x1b[1;91m|  \x1b[1;97mbangsat12346'
time.sleep(18)
print '\x1b[1;91m[ \x1b[1;92mOK✓\x1b[1;91m ]  \x1b[1;97m100011772787272  \x1b[1;91m|  \x1b[1;97m123456'
time.sleep(8)
print '\x1b[1;91m[ \x1b[1;92mOK✓\x1b[1;91m ]  \x1b[1;97m100067398376882  \x1b[1;91m|  \x1b[1;97m20102002'
time.sleep(10)
print '\x1b[1;91m[ \x1b[1;93mCP+\x1b[1;91m ]  \x1b[1;97m100011122455899  \x1b[1;91m|  \x1b[1;97mSiska123'
time.sleep(8)
print '\x1b[1;91m[ \x1b[1;92mOK✓\x1b[1;91m ]  \x1b[1;97m100067282727774  \x1b[1;91m|  \x1b[1;97mAngga123'
time.sleep(6)
print '\x1b[1;91m[ \x1b[1;93mCP+\x1b[1;91m ]  \x1b[1;97m100087299907544  \x1b[1;91m|  \x1b[1;97mSitepu12345'
time.sleep(10)
print '\x1b[1;91m[ \x1b[1;93mCP+\x1b[1;91m ]  \x1b[1;97m100017272726262  \x1b[1;91m|  \x1b[1;97mYudha12346'
time.sleep(9)
print '\x1b[1;91m[ \x1b[1;92mOK✓\x1b[1;91m ]  \x1b[1;97m100046677278282  \x1b[1;91m|  \x1b[1;97mMaya123'
time.sleep(6)
print '\x1b[1;91m[ \x1b[1;93mCP+\x1b[1;91m ]  \x1b[1;97m100092772728929  \x1b[1;91m|  \x1b[1;97mFajar1234'
raw_input('\n\x1b[1;91m[ \x1b[1;97mSelesai \x1b[1;91m]')
