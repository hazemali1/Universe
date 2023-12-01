// var gg = document.querySelector('.galaxies');
	
// gg.addEventListener('click', function(event) {
// 	gg.classList.toggle('click_g');
// 	event.stopPropagation();
// });

// var ss = document.querySelector('.galaxy');

// ss.addEventListener('click', function(event) {
// 	ss.classList.toggle('click_s');
// 	event.stopPropagation();
// });

// var pp = document.querySelector('.solar_system');

// pp.addEventListener('click', function(event) {
// 	pp.classList.toggle('click_p');
// 	event.stopPropagation();
// });

var s = document.querySelector('.word');
var ss = document.querySelector('.display');

s.addEventListener('click', function(event) {
	ss.classList.toggle('displaying');
	event.stopPropagation();
});

var p = document.querySelector('*');
// var pp = document.querySelector('.Milky_Way *');

p.addEventListener('click', function(event) {
	var xx = event.target.classList[0];
	var zz = "." + String(xx) + ' *';
	var dd = "." + String(xx) + "_details";
	console.log(zz);
	console.log(dd);
	var vv = document.querySelector(zz);
	var ddd = document.querySelector(dd);
	if (vv)
		vv.classList.toggle('displaying');
});

var ps = document.querySelector('*');
// var pps = document.querySelector('.Milky_Way *');
var xxs;

ps.addEventListener('click', function(event) {
	console.log(event.target.classList[0]);
	console.log(xxs);
	console.log("---------------");
	var hh = event.target.classList[0];
	console.log(hh);
	var test = document.querySelector('button');
	if (!test && hh && hh != "main" && hh != "first" && hh != "galaxies" && hh != "img" && hh != "about" && hh[0] != 'i') {
		var newButton = document.createElement('button');
		newButton.textContent = 'See Details';
		document.body.appendChild(newButton);
	}

	console.log(event.target.classList);
	var cc = document.querySelector('button');
	var ccc = document.querySelector('.galaxies');
	if (event.target.classList[0]) {
		xxs = event.target.classList[0];
		console.log("changed");
	}
	console.log(event.target.classList[0]);
	console.log(xxs);
	bb = document.querySelector('.second');
	var ii = document.querySelector('.swimming');
	cc.addEventListener('click', function() {

	
		
		// var zzs = "." + String(xxs) + ' *';
		var dds = "." + String(xxs) + "_details";
		var dddd = "." + String(xxs) + "_details" + " *";
		// console.log(zzs);
		// console.log(dds);
		// var vvs = document.querySelector(zzs);
		var ddds = document.querySelector(dds);
		var dddds = document.querySelector(dddd);
		// console.log(ddds);
		ddds.classList.toggle('displayingttr');
		dddds.classList.toggle('displayingtr');
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