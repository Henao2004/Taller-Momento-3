let prevScrollPos = window.pageYOffset;

window.onscroll = function() {
    let currentScrollPos = window.pageYOffset;
    if (prevScrollPos > currentScrollPos) {
        document.getElementById("navbar").style.top = "0";
    } else {
        document.getElementById("navbar").style.top = "-100px"; // Oculta el navbar al hacer scroll hacia abajo
    }
    prevScrollPos = currentScrollPos;
}
document.addEventListener('DOMContentLoaded', function() {
    var myCarousel = new bootstrap.Carousel(document.getElementById('myCarousel'), {
        interval: 4000, 
        wrap: true, 
        keyboard: false, 
    });
});
