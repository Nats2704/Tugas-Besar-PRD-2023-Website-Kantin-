// Toggle Class Active
const navbarNav = document.querySelector(".navbar-nav");
// Saat Hamburger Menu diKlik
document.querySelector("#hamburger-menu").onclick = () => {
  navbarNav.classList.toggle("active");
};

// Klik di Luar SideBar untuk Menghilangkan Navbar
const hamburger = document.querySelector("#hamburger-menu");

document.addEventListener("click", function (e) {
  if (!hamburger.contains(e.target) && !navbarNav.contains(e.target)) {
    navbarNav.classList.remove("active");
  }
});
