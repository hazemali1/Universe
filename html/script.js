var s = document.querySelector('.word');
var ss = document.querySelector('.display');

s.addEventListener('click', function(event) {
	ss.classList.toggle('displaying');
	event.stopPropagation();
});

var p = document.querySelector('*');

p.addEventListener('click', function(event) {
	var xx = event.target.classList[0];
	var zz = "." + String(xx) + ' *';
	var dd = "." + String(xx) + "_details";
	var vv = document.querySelector(zz);
	var ddd = document.querySelector(dd);
	if (vv)
		vv.classList.toggle('displaying');
});

var ps = document.querySelector('*');
var xxs;

ps.addEventListener('click', function(event) {

	var hh = event.target.classList[0];
	var test = document.querySelector('button');
	if (!test && hh && hh != "main" && hh != "first" && hh != "galaxies" && hh != "img" && hh != "about" && hh[0] != 'i') {
		var newButton = document.createElement('button');
		newButton.textContent = 'See Details';
		document.body.appendChild(newButton);
	}

	var cc = document.querySelector('button');
	var ccc = document.querySelector('.galaxies');
	if (event.target.classList[0]) {
		xxs = event.target.classList[0];
	}

	bb = document.querySelector('.second');
	var ii = document.querySelector('.swimming');
	cc.addEventListener('click', function() {

	
		
		var dds = "." + String(xxs) + "_details";
		var dddd = "." + String(xxs) + "_details" + " img";
		var ddddd = "." + String(xxs) + "_details" + " pre";
		var ddds = document.querySelector(dds);
		var dddds = document.querySelector(dddd);
		var ddddds = document.querySelector(ddddd);
		ddds.classList.toggle('displayingttr');
		dddds.classList.toggle('displayingtr');
		ddddds.classList.toggle('displayingcon');
		cc.classList.toggle('displayinggtr');
		ccc.classList.toggle('displayinggtr');
		ii.classList.toggle('displayingg');
		bb.classList.toggle('index');
	});
});

document.querySelector('h2').addEventListener('click', function() {
    location.reload();
});
document.querySelector('.img').addEventListener('click', function() {
    location.reload();
});


var a = document.querySelector('h3');
var aa = document.querySelector('.about');

a.addEventListener('click', function(event) {
	aa.classList.toggle('visable');
	event.stopPropagation();
});
