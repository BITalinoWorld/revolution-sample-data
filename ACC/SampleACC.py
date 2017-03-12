x=loadtxt('SampleACC.txt')[:,-1]
sx=smooth(x,500)[500:10500]
plot(2*((x[500:10500]-sx.min())/(sx.max()-sx.min())-.5),color = '#cccccc')
plot(2*((sx-sx.min())/(sx.max()-sx.min())-.5),'k')
ylim([-3,3])
ylabel('g')
xlabel('t (ms)')
legend(['RAW', 'FILT'])
savefig('SampleACC.png',dpi=300)
