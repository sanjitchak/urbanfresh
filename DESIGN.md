---
name: UrbanFresh Rice Mills
description: A practical mill sample book for serious rice buyers.
colors:
  mill-green: "oklch(31% 0.075 158)"
  field-green: "oklch(43% 0.09 151)"
  rice-gold: "oklch(76% 0.12 82)"
  husk-paper: "oklch(96% 0.018 88)"
  warm-sheet: "oklch(98% 0.01 88)"
  ink: "oklch(24% 0.035 158)"
  muted-ink: "oklch(43% 0.035 158)"
  rule: "oklch(85% 0.025 88)"
typography:
  display:
    fontFamily: "Bitter, Rockwell, Georgia, serif"
    fontSize: "clamp(2.8rem, 6vw, 5.5rem)"
    fontWeight: 650
    lineHeight: 1.02
  headline:
    fontFamily: "Bitter, Rockwell, Georgia, serif"
    fontSize: "clamp(2rem, 4vw, 3.5rem)"
    fontWeight: 650
    lineHeight: 1.1
  body:
    fontFamily: "Source Sans 3, Segoe UI, sans-serif"
    fontSize: "1rem"
    fontWeight: 400
    lineHeight: 1.65
rounded:
  field: "4px"
  panel: "8px"
spacing:
  xs: "8px"
  sm: "16px"
  md: "24px"
  lg: "32px"
  xl: "48px"
  2xl: "80px"
  3xl: "120px"
components:
  button-primary:
    backgroundColor: "{colors.rice-gold}"
    textColor: "{colors.ink}"
    rounded: "{rounded.field}"
    padding: "15px 24px"
  field:
    backgroundColor: "{colors.warm-sheet}"
    textColor: "{colors.ink}"
    rounded: "{rounded.field}"
    padding: "13px 14px"
---

# Design System: UrbanFresh Rice Mills

## 1. Overview

**Creative North Star: The Mill Sample Book.**

The site should feel like a well-used trade sample book brought online: sturdy, specific, easy to scan and focused on the buying requirement. Product photography and plain commercial language lead. Decoration stays quiet. A visitor should quickly understand what UrbanFresh supplies, which details affect a quote and how to send those details.

## 2. Colors

Mill Green anchors navigation, headings and dark sections. Rice Gold marks the primary action and small pieces of useful emphasis. Husk Paper is the main page surface, with Warm Sheet used for forms and reading panels. Ink and Muted Ink are green-tinted neutrals. New colors must be declared in OKLCH and must meet WCAG AA contrast in their actual pairing.

## 3. Typography

Bitter gives headings a practical slab-serif voice associated with ledgers, sacks and printed trade material without imitating a heritage luxury brand. Source Sans 3 keeps body copy and forms highly readable. Body copy stays between 45 and 75 characters per line. Tiny uppercase labels are rare and used only where they improve wayfinding.

## 4. Elevation

The system is flat at rest. Structure comes from spacing, rules and tonal changes. Shadows appear only for the sticky header and active interactive states. Corners are modest at 4px or 8px. Large pill shapes, glass effects, decorative gradients and concentric-circle ornaments do not belong.

## 5. Components

Primary buttons use Rice Gold with dark text and a compact 4px corner. Secondary actions are text links or outlined buttons. Product entries use a large image and ledger-style text rather than a field of identical floating cards. Information panels and quote fields use hairline borders. Every control includes default, hover, focus, disabled, loading, success and error behavior where applicable.

## 6. Do's and Don'ts

Do show numbered rice varieties early, write like a mill representative and make quantity, destination and packaging easy to provide. Do keep keyboard focus visible, touch targets at least 44px and motion optional. Do use varied section rhythm and useful asymmetry.

Do not use unsupported certificates, capacity or export claims. Do not expose SEO strategy in visitor copy. Do not use em dashes. Do not use copied competitor images, repetitive card grids, generic startup phrases, side-stripe accents or decorative motion.
