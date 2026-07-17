# UI Components — Interactions & Pitfalls Reference

> **CRITICAL RULE: Copy template verbatim — zero improvisation. Check ux-patterns-for-developers before writing component behavior.**

---

## 08 · SCROLL REVEAL (section entrance)

### Spec
```
Trigger:    IntersectionObserver threshold 0.1, rootMargin 0px 0px -40px 0px
Effect:     opacity 0→1 + translateY(20px)→0
Duration:   350ms ease-enter
Class:      .reveal → add .visible on enter
```

### Template
```css
.reveal {
  opacity: 0; transform: translateY(20px);
  transition: opacity 350ms cubic-bezier(0,0,0.2,1),
              transform 350ms cubic-bezier(0,0,0.2,1);
}
.reveal.visible { opacity: 1; transform: none; }
@media (prefers-reduced-motion: reduce) {
  .reveal { opacity: 1 !important; transform: none !important; transition: none !important; }
}
```

### JS
```js
const observer = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      entry.target.classList.add('visible');
      observer.unobserve(entry.target);
    }
  });
}, { threshold: 0.1, rootMargin: '0px 0px -40px 0px' });
document.querySelectorAll('.reveal').forEach(el => observer.observe(el));
```

---

## 09 · VERIFICATION CHECKLIST (run after every component change)

```js
// Paste in browser console — all must pass before deliver
const ok = {
  bg:        getComputedStyle(document.body).backgroundColor, // ≠ rgba(0,0,0,0)
  sheets:    document.styleSheets.length,                     // > 0
  touchFail: [...document.querySelectorAll('a,button')]
               .filter(el=>{const b=el.getBoundingClientRect();
                 return b.width>0&&b.height<44;}).length,     // === 0
  h1TopPct:  Math.round(document.querySelector('h1')
               .getBoundingClientRect().top/window.innerHeight*100), // < 45
  maxWidth:  getComputedStyle(document.querySelector('.hero-content')||
               document.querySelector('.nav-inner')).maxWidth,       // 1280px
};
console.table(ok);
```

---

## PITFALLS

```
□ Improvising component CSS → always copy template above, never write from scratch
□ Missing max-width on sections → content bleeds to viewport edge on ultrawide
□ Hero display:grid + 1fr row → content floats in void at tall viewports → use display:block
□ Touch targets: min-height alone doesn't work if parent is flex with align-items:center
  → use height:44px + display:flex + align-items:center on the link itself
□ CSS patch corruption: 3+ patches on same block → nested rules → white page
  → after 2 patches fail, rewrite full file with write_file
□ self-closing divs used as grid rows → don't, use display:none or remove
```
