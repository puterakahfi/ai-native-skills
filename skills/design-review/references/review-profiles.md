# Review Profiles

Use this reference after routing. A review profile changes gate priority, thresholds, and evidence expectations without duplicating universal design principles.

## Shared rule

A profile is not a style preset. It describes the job of the surface, the viewing context, and the risks that deserve higher review weight.

## Web marketing

Primary jobs:

```text
communicate value quickly
establish credibility
create a coherent persuasion path
make the primary action obvious
remain readable and usable across viewports
```

Prioritize:

- first-impression clarity;
- value proposition and message hierarchy;
- hero or opening composition;
- trust and proof integrity;
- CTA prominence and action honesty;
- page rhythm and section sequencing;
- responsive navigation and content reflow;
- performance and runtime health on the reviewed route.

Common risks:

- generic AI-template composition;
- excessive decorative depth with weak content hierarchy;
- equal-weight sections and cards;
- fake or unverified proof;
- oversized display typography that harms mobile comprehension;
- CTA labels that promise state or outcomes the product cannot provide.

## Web application

Primary jobs:

```text
support task completion
preserve context
make system state visible
keep controls discoverable and predictable
handle realistic data density and failure states
```

Prioritize:

- task hierarchy and information architecture;
- navigation and orientation;
- control selection and component fit;
- loading, empty, error, success, disabled, and permission states;
- keyboard, pointer, and touch behavior where relevant;
- data density, scanning, and comparison;
- adaptive layout at realistic breakpoints;
- runtime integrity throughout the reviewed flow.

Common risks:

- forcing desktop components onto narrow screens;
- hiding primary options to solve overflow instead of adapting the component;
- overlapping controls or invisible previous/next affordances;
- ambiguous state, destructive actions, or stale continuation labels;
- polished static state with broken interaction or runtime errors.

## Mobile application

Primary jobs:

```text
support one-handed and touch-first use
preserve task context on constrained screens
respect platform and device conventions
handle keyboard, safe areas, gestures, and interruptions
```

Prioritize:

- touch target reachability and non-overlap;
- navigation model and back behavior;
- safe areas, system bars, and device cutouts;
- keyboard appearance, dismissal, and field visibility;
- gesture discoverability and alternatives;
- content priority and progressive disclosure;
- dynamic text, localization, and orientation resilience;
- loading, offline, permission, and interruption states.

Common risks:

- desktop navigation compressed into mobile;
- hidden horizontal overflow without affordances;
- controls placed outside comfortable reach;
- gesture-only interaction;
- modal or keyboard traps;
- fixed-height layouts that break with content growth.

## Desktop application

Primary jobs:

```text
support sustained, high-density work
make multi-panel relationships understandable
enable efficient keyboard and pointer workflows
remain stable during resizing and multi-window use
```

Prioritize:

- window resizing and minimum-size behavior;
- density and scanability;
- panel hierarchy, selection, and persistent context;
- keyboard shortcuts, menus, focus, and selection models;
- drag, resize, hover, and context-menu behavior where relevant;
- long-running state, background operations, and recovery;
- multi-window or multi-document consistency when applicable.

Common risks:

- web-dashboard patterns that ignore desktop conventions;
- excessive whitespace that reduces working density;
- ambiguous selected panel or active document;
- hover-only critical actions;
- resizing that clips or detaches controls from content.

## Static marketing visual

Includes posters, flyers, banners, ads, social creatives, stories, thumbnails, and campaign cards.

Primary jobs:

```text
communicate one dominant message
attract attention without sacrificing comprehension
preserve brand and product fidelity
survive the intended channel, crop, and export size
```

Prioritize:

- message recognition at actual display size;
- focal point and visual flow;
- typography at intended viewing distance;
- offer, price, date, contact, and CTA accuracy;
- brand, logo, product, packaging, and face fidelity;
- crop, safe-area, bleed, and interface-overlay safety;
- export sharpness and channel suitability.

Common risks:

- judging only from a large canvas instead of feed or story size;
- decorative model or background competing with the product;
- unreadable small copy;
- altered product, logo, face, price, or contact details;
- composition that works in the editor but fails after crop.

## Presentation

Primary jobs:

```text
support spoken or self-guided comprehension
maintain narrative continuity across slides
make each slide understandable at room or screen-share scale
```

Prioritize:

- one dominant idea per slide;
- narrative progression;
- title and key-data legibility;
- chart and diagram comprehension;
- repeated layout consistency without monotony;
- source and claim integrity;
- room-distance or screen-share readability.

Common risks:

- document paragraphs pasted onto slides;
- charts that require close reading;
- every slide using the same visual weight;
- decorative images unrelated to the argument;
- inconsistent titles, margins, or data emphasis.

## Profile weighting guidance

Weights may change by profile, but gate definitions must not be rewritten to force a preferred style.

```text
web marketing       content/hierarchy/CTA/responsive/runtime receive higher weight
web application     task flow/states/components/accessibility/runtime receive higher weight
mobile application  touch/navigation/adaptation/states receive higher weight
desktop application density/context/keyboard/resize receive higher weight
static marketing    message/fidelity/composition/legibility/export receive higher weight
presentation        narrative/legibility/data clarity/consistency receive higher weight
```

When a target spans profiles, choose one primary profile and declare secondary concerns. Do not average two unrelated scorecards without explaining the weighting.