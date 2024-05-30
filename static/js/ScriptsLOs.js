gsap.registerPlugin(ScrollTrigger, ScrollToPlugin);
    
      const $container = document.querySelector('.container');
      const $sections = gsap.utils.toArray("[data-scroll='section']");
      const $images = gsap.utils.toArray("[data-scroll='image']");
    
      // Anchor Nav
      document.querySelectorAll(".anchor").forEach(anchor => {
      anchor.addEventListener("click", function(e) {
      e.preventDefault();
      const targetId = e.target.getAttribute("href");
      const target = document.querySelector(targetId);
      if (target) {
      const containerRect = $container.getBoundingClientRect();
      const targetRect = target.getBoundingClientRect();
      const scrollX = targetRect.left - containerRect.left;

      gsap.to($container, {
        scrollTo: { x: scrollX, autoKill: false },
        duration: 1
      });
    }
  });
});
    
      // Horizontal Scroll 
      const offset = -100 * ($sections.length - 1);
      const scroll = 3000;
      const scrollTween = gsap.to($sections, {
        xPercent: offset,
        ease: "none",
        scrollTrigger: {
          trigger: $container,
          pin: true,
          scrub: 0.5,
          end: `+=${scroll}`
        }
      });
    
      // Parallax Image 
      $images.forEach($image => {
        const intensity = Number($image.dataset.intensity);
        gsap.fromTo(
          $image,
          { x: gsap.utils.interpolate("0%", "-100%", intensity) },
          {
            x: gsap.utils.interpolate("0%", "100%", intensity),
            ease: "none",
            scrollTrigger: {
              trigger: $image,
              containerAnimation: scrollTween,
              start: "left right",
              end: "right left",
              scrub: true,
              invalidateOnRefresh: true,
            },
          }
        );
      });
    
      // Text Animation
      window.onload = function() {
        const tl = gsap.timeline({delay: 1}),
              firstBg = document.querySelectorAll('.text__first-bg'),
              secBg = document.querySelectorAll('.text__second-bg'),
              word = document.querySelectorAll('.text__word');
        
        tl.to(firstBg, { duration: 0.2, scaleX: 1 })
          .to(secBg, { duration: 0.2, scaleX: 1 })
          .to(word, { duration: 0.1, opacity: 1 }, "-=0.1")
          .to(firstBg, { duration: 0.2, scaleX: 0 })
          .to(secBg, { duration: 0.2, scaleX: 0 });
      }