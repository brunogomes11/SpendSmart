const toggleBtn = document.getElementsByClassName("toggle-btn")[0];
const navbarLinks = document.getElementsByClassName("navbar-links")[0];
const enterLinks = document.getElementsByClassName("enter-links")[0];
toggleBtn.addEventListener("click", function () {
    navbarLinks.classList.toggle("active");
    enterLinks.classList.toggle("active");
});
