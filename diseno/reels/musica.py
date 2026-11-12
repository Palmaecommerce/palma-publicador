# Pista original generada por código (sin derechos de terceros): beat pop suave a 112 bpm
import numpy as np, wave, sys
sr=44100; dur=float(sys.argv[2]) if len(sys.argv)>2 else 9.2; bpm=112; beat=60/bpm
t=np.arange(int(sr*dur))/sr; out=np.zeros_like(t)
def env(n,a=0.005,d=0.25):
    x=np.arange(n)/sr; return np.minimum(1,x/a)*np.exp(-x/d)
def add(sig,start):
    i=int(start*sr)
    if i>=len(out): return
    j=min(len(out),i+len(sig)); out[i:j]+=sig[:j-i]
rng=np.random.default_rng(3)
# acordes (Am F C G) en pad suave
chords=[[220,261.6,329.6],[174.6,220,261.6],[261.6,329.6,392],[196,246.9,293.7]]
bar=4*beat
for k in range(int(dur/bar)+1):
    c=chords[k%4]; n=int(bar*sr); x=np.arange(n)/sr
    pad=sum(np.sin(2*np.pi*f*x)+0.3*np.sin(2*np.pi*2*f*x) for f in c)*0.05*np.minimum(1,x/0.08)*np.exp(-x/3)
    add(pad,k*bar)
    # bajo
    for b in range(4):
        m=int(beat*sr*0.9); xb=np.arange(m)/sr; add(0.18*np.sin(2*np.pi*c[0]/2*xb)*env(m,0.005,0.2), k*bar+b*beat)
    # arpegio
    for s in range(8):
        f=c[s%3]*2; m=int(beat/2*sr); xa=np.arange(m)/sr; add(0.05*np.sign(np.sin(2*np.pi*f*xa))*env(m,0.002,0.08), k*bar+s*beat/2)
nb=int(dur/beat)+1
for b in range(nb):
    st=b*beat; m=int(0.3*sr); x=np.arange(m)/sr
    kick=np.sin(2*np.pi*(50+90*np.exp(-x*30))*x)*np.exp(-x*9)*0.5; add(kick,st)
    if b%2==1: add(rng.normal(0,1,m)*np.exp(-x*18)*0.18,st)
    for h in range(2):
        mh=int(0.05*sr); add(rng.normal(0,1,mh)*np.exp(-np.arange(mh)/sr*80)*0.06*np.where(np.arange(mh)%2,1,-1),st+h*beat/2)
fade=np.minimum(1,np.minimum(t/0.3,(dur-t)/0.8)); out*=fade
out=out/np.max(np.abs(out))*0.8
w=wave.open(sys.argv[1],'w'); w.setnchannels(1); w.setsampwidth(2); w.setframerate(sr); w.writeframes((out*32767).astype(np.int16).tobytes()); w.close()
