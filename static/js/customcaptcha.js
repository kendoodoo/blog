document.head.innerHTML += "<style>#thuntaduns {pointer-events: none;}.d {display: flex; }#captchaverify{ font-size: 20px;width: 70px; text-align: center; outline: none;}#cvs {background: url('data:image/gif;base64,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');}</style>", ooh = [" ", "  ", "  "], oohnum = [16, 15, 26, 25, 24, 14, 27, 28, 29, 13, 14, 12, 9, 28];
var e;
function reloadcaptcha() {
  var c = document.getElementById("cvs");
  c.style.webkitFilter = "blur(0.6px)";
  c.width = 160, c.height = 40;
  var d = c.getContext("2d");
  d.font = "italic bold 28px san-serif", d.textAlign = "center", d.fillStyle = "white", d.rotate(oohnum[0 | Math.random() * ooh.length] * Math.PI / 1160);
  e = Math.random().toString(36).slice(-6).split("").join(ooh[0 | Math.random() * ooh.length]);
  d.fillText(e, c.width / 2, c.height / 1.55);
  let {
    width: a
  } = d.measureText(e);
  d.fillStyle = "red", d.rotate(-2 * Math.PI / 1160), d.fillRect(c.width / 5, c.height / 1.65, a, 1), d.fillStyle = "blue", d.rotate(-3 * Math.PI / 360), d.fillRect(c.width / 6, c.height / 2, a, 1.8)
}
reloadcaptcha();

function chekhim() {
  if (document.querySelector('#captchaverify').value !== e.replace(/\s/g, '')) {
    document.querySelector('#thuntaduns').value = "";
  } else {
    document.querySelector('#thuntaduns').value = Math.random();
  }
}