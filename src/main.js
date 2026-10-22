import "./style.css";

const header = document.querySelector(".site-header");

const onScroll = () => {
  header?.classList.toggle("is-scrolled", window.scrollY > 12);
};

onScroll();
window.addEventListener("scroll", onScroll, { passive: true });
