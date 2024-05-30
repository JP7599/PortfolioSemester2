console.clear();

gsap.registerPlugin(ScrollTrigger);

window.addEventListener("load", () => {
  gsap
    .timeline({
      scrollTrigger: {
        trigger: ".wrapper",
        start: "top top",
        end: "+=150%",
        pin: true,
        scrub: true,
        markers: true,
        onUpdate: self => {
          if (self.progress === 1) {
            document.querySelector("#home").classList.add("show-section");
            document.querySelector(".image-container").style.display = "none";
            document.querySelector(".section.hero").style.display = "none";
          }
        }
      }
    })
    .to(".image-container img", {
      scale: 2,
      y: 200, // Adjust this value to zoom in a bit higher than the head
      transformOrigin: "center center",
      ease: "power1.inOut"
    });
});



