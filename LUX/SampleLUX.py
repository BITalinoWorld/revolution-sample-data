x=loadtxt('SampleLUX.txt')[:,-1]
plot(x[5000:-5000]/1023.*100,'k')
ylabel('%')
xlabel('t (ms)')
savefig('SampleLUX.png',dpi=300)
