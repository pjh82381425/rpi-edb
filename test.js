let size = 86;
let columns = Array.from(document.getElementsByClassName('column'));
let d, c;
let classList = [ 'visible', 'close', 'far', 'far', 'distant', 'distant' ];
let use24HourClock = false;

function padClock(p, n) {
	return p + ('0' + n).slice(-2);
}

function getClock() {
	d = new Date();
	return [
			use24HourClock ? d.getHours() : (d.getHours() % 12 || 12),
			d.getMinutes(),
			d.getSeconds()
		]
		.reduce(padClock, '');
}

function getClass(n, i2) {
	return classList.find((class_, classIndex) => Math.abs(n - i2) === classIndex) || '';
}

let loop = setInterval(() => {
	c = getClock();

	columns.forEach((ele, i) => {
		let n = +c[i];
		let offset = -n * size;
		ele.style.transform = `translateY(calc(50vh + ${offset}px - ${size / 2}px))`;
		Array.from(ele.children).forEach((ele2, i2) => {
			ele2.className = 'num ' + getClass(n, i2);
			let blurAmount = Math.abs(n - i2) * 2;
			ele2.style.filter = `blur(${blurAmount}px)`;
		});
	});
}, 200 + Math.E * 10);