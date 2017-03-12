x=loadtxt('SampleECG.txt')[:,-1]
#sx=smooth(x,50)
plot(x[-9000:-4000]/1024./1.1*3.3-1.5, 'k')
ylim([-1.5,1.5])
ylabel('mV')
xlabel('t (ms)')
savefig('SampleECG.png',dpi=300)
