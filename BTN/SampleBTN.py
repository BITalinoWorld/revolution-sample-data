x=loadtxt('SampleBTN.txt')[:,1]
plot(x[5000:8000],'k')
xlabel('t (ms)')
ylim([-.01, 1.01])
savefig('SampleBTN.png',dpi=300)
