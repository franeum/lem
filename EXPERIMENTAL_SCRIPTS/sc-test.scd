(
s = Server.local;
s.waitForBoot({
	{SinOsc.ar([440,440], 0.0, 0.5)}.play;
})
)