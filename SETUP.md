# Installing the GitHub Black Edition profile

This package is intended for **https://github.com/IfBilal/IfBilal**.

1. While logged into `IfBilal`, create a **public** repository named exactly `IfBilal` (or open it if it exists).
2. Put `README.md` at the repository root and upload the **entire `assets/` directory**. GitHub will automatically display the README on the account's Overview tab.
3. Visit **https://github.com/IfBilal**. Check the visual layout on desktop and mobile, and click the project artwork to test its repository links.
4. Keep the SVG filenames and the GIF path unchanged unless you also update `README.md`.

## What is inside

```text
IfBilal/
├── README.md
└── assets/
    ├── hero.svg
    ├── focus.gif
    ├── contact-github.svg
    ├── contact-linkedin.svg
    ├── contact-email.svg
    ├── project-skyeye.svg
    ├── project-rahnuma.svg
    ├── project-codegrapher.svg
    ├── project-real-estate.svg
    ├── toolbox.svg
    ├── evidence.svg
    └── footer.svg
```

The extra `tools/build.py` file in the download is the **editable generator** for all of these assets. To regenerate the visuals, install `pip install pillow cairosvg` and run `python tools/build.py` from this directory. Only the SVGs and `focus.gif` need to be committed; the `.png` files in this package are preview exports and are not required for GitHub.

## Design rules

- **Palette:** black `#090909`, charcoal `#101010`, off-white `#F1EEE8`, warm muted accent `#CEBA97`.
- **Motion:** one restrained locally stored GIF; a tiny optional SVG breathing dot in the hero. All content remains legible if SVG animation is disabled.
- **No JavaScript, iframes, CSS injections, remote stat services, or external art hosting.**
- **Content:** role, experiences, and metrics were taken from the supplied CV; linked repositories were checked against the public GitHub account. CV contact phone is intentionally omitted from the public profile.

This package does not modify the live GitHub repository or your account settings.
