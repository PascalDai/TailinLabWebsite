// CSS 加载器函数
function loadCSS(href) {
  var cssLink = document.createElement("link");
  cssLink.rel = "stylesheet";
  cssLink.href = href;
  var head = document.getElementsByTagName("head")[0];
  head.appendChild(cssLink);
}

// 在 DOMContentLoaded 后加载非关键 CSS
document.addEventListener("DOMContentLoaded", function () {
  loadCSS("/assets/css/material-kit-pro.min.css");
  loadCSS("/assets/css/nucleo-icons.css");
  loadCSS("/assets/css/nucleo-svg.css");
  loadCSS("/assets/css/nativecode.css");
  loadCSS("/assets/css/output.css");
});
