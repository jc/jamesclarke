# jamesclarke site workflow

This codebase builds a static Hyde site with Docker and ships the generated `public/` folder through Vercel. The repo itself stays committed only to the source files; `public/` is ignored and refreshed per–deploy.

## Prerequisites

- Docker + docker-compose
- Vercel CLI (`npm i -g vercel`) authenticated against the `jamesclarke` project

Run `vercel pull --yes` once per environment (or whenever Vercel settings change) so the local CLI has the right project/production config cached.

## Build the site

```bash
docker-compose build jamesclarkenet
docker-compose run --rm jamesclarkenet
```

The compose file mounts the repo at `/usr/src/jamesclarke` and `./public` at `/public`, so Hyde runs inside the container and writes new artifacts straight into `public/`.

## Deploy

1. **Preview**

   ```bash
   vercel deploy public
   # or skip Vercel’s rebuild if you trust the local output:
   vercel deploy --prebuilt public
   ```

   Inspect the preview URL that Vercel returns.

2. **Production**

   ```bash
   vercel deploy --prod public
   # or:
   vercel deploy --prod --prebuilt public
   ```

   This publishes the current `public/` contents to the live domain once you are satisfied with the preview.
