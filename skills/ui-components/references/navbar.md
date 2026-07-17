<!-- HARD RULES reminder -->
<!-- Copy template verbatim. Check ux-patterns-for-developers for behavior spec. -->

## 01 · NAVBAR

### Spec
```
height:         64px
position:       sticky top:0 z-index:100  ← CSS-only, no JS scroll jank
background:     transparent → blur on scroll
border:         none → box-shadow on scroll (more depth than border)
max-width:      var(--content-max, min(1200px,90vw)) centered
items:          Work · About · Contact  (max 7 per Miller's Law)
```

### Template
```css
/* ── NAV — from navigation-menu pattern (uxpatterns.dev) ── */
nav#site-nav {
  position: sticky; top: 0; z-index: 100;
  height: 64px;
  background: transparent;
  transition: background var(--dur-fast) var(--ease-standard),
              box-shadow var(--dur-fast) var(--ease-standard);
}
nav#site-nav.scrolled {
  box-shadow: 0 1px 0 var(--border), 0 4px 16px rgba(0,0,0,0.4);
  backdrop-filter: blur(16px);
  background: rgba(9,9,8,0.92);
}
.nav-inner {
  max-width: var(--content-max, min(1200px,90vw));
  margin: 0 auto; height: 100%;
  display: flex; align-items: center; justify-content: space-between;
  padding: 0 var(--sp-6);
}
.nav-links { display: flex; gap: var(--sp-5); list-style: none; }
.nav-links a {
  font-size: var(--text-sm); color: var(--subtle);
  text-decoration: none; padding: var(--sp-2) var(--sp-3);
  border-radius: 6px;
  transition: color var(--dur-fast) var(--ease-standard),
              background var(--dur-fast) var(--ease-standard);
}
.nav-links a:hover { color: var(--bright); background: var(--surface); }
.nav-links a:focus-visible { outline: 2px solid var(--accent); outline-offset: 2px; }
```

### HTML
```html
<!-- skip link — first focusable element per navigation-menu pattern -->
<a href="#main" class="skip-link">Skip to content</a>

<nav id="site-nav" aria-label="Main navigation">
  <div class="nav-inner">
    <a href="#" class="nav-logo">pkahfi.</a>
    <ul class="nav-links" role="list">
      <li><a href="#work" aria-current="page">Work</a></li>
      <li><a href="#about">About</a></li>
      <li><a href="#contact">Contact</a></li>
    </ul>
    <button class="nav-hamburger" aria-label="Open menu" aria-expanded="false" aria-controls="mobile-menu">
      <span class="sr-only">Open menu</span>
      <!-- icon -->
    </button>
  </div>
</nav>
```

### Behavior (from navigation-menu uxpattern)
```
Scroll:     add .scrolled class via IntersectionObserver or scroll event
Hamburger:  aria-expanded toggles true/false; aria-label updates to "Close menu"
Keyboard:   Escape closes mobile menu; focus returns to trigger
Click-out:  closes mobile menu
Active:     aria-current="page" on current section link
```

### JS
```js
const nav = document.querySelector('#site-nav');
window.addEventListener('scroll', () => {
  nav.classList.toggle('scrolled', window.scrollY > 20);
}, { passive: true });
```

### Skip Link CSS
```css
.skip-link {
  position: absolute; top: -100%; left: var(--sp-6);
  background: var(--accent); color: var(--bg);
  padding: var(--sp-4) var(--sp-5); font-weight: 700;
  font-size: var(--text-sm); border-radius: 0 0 6px 6px;
  text-decoration: none; z-index: 200;
  transition: top 0.2s;
}
.skip-link:focus { top: 0; }
```
