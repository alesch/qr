# qr

QR code generator and short-link redirector for `qr.schenkman.info`.

## What this is

`generate.py` produces a QR code (SVG, PNG, and EPS) that encodes a short
URL, currently `http://qr.schenkman.info/a`. That domain is deployed on
Vercel, which redirects requests to the real destination according to
`vercel.json`. This lets the printed/physical QR code stay valid forever
even if the destination it points to changes — only the Vercel redirect
config needs to be updated.

## Generating a QR code

Dependencies are managed with [mise](https://mise.jdx.dev/) and `pip`.

```sh
mise install       # installs Python 3.12 and the Vercel CLI
mise run install   # pip install . (qrcode + cairosvg)
mise run generate  # runs generate.py
```

This writes `qr.svg`, `qr.png`, and `qr.eps` (or `<name>.*` if a filename
argument is passed to `generate.py`) encoding `http://qr.schenkman.info/a`.

## Deployment

The `qr.schenkman.info` domain is deployed on [Vercel](https://vercel.com).
`vercel.json` defines the redirect rules served at that domain — there is no
application code to deploy, only the redirect config.

```sh
vercel          # deploy a preview
vercel --prod   # deploy to production (qr.schenkman.info)
```

## Redirects

| Source                       | Destination                             |
| ----------------------------- | ---------------------------------------- |
| `http://qr.schenkman.info/a` | `https://alesch.github.io/memorial/`     |

The destination is a static site from the
[`alesch/memorial`](https://github.com/alesch/memorial) repository, hosted
via GitHub Pages. To point the QR code at a different destination, update
the `destination` field for the matching `source` in `vercel.json` and
redeploy with `vercel --prod`; the QR code image itself never needs to be
regenerated.
