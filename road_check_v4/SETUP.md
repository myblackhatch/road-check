# Road Check v4: setup (about 15 minutes)

## 1. Put it on GitHub Pages (once)
1. Sign in at github.com → **+** (top right) → **New repository**.
2. Name it `road-check`, set it to **Public** (free Pages needs public), click **Create repository**.
3. On the new repo page click **uploading an existing file**. Drag in **all files from this folder**:
   `index.html`, `manifest.webmanifest`, `sw.js`, `icon-192.png`, `icon-512.png`, `icon-512-maskable.png`, `apple-touch-icon.png`.
   Click **Commit changes**.
4. Repo **Settings** → **Pages** → under "Build and deployment" choose **Deploy from a branch**, branch **main**, folder **/ (root)** → **Save**.
5. Wait 1–2 minutes. Your app is at `https://YOUR-USERNAME.github.io/road-check/`.

Nothing personal is in these files: just highway camera locations. **Never put your TomTom key in the files.** It is typed into the app and stays on your phone.

## 2. Install on your Android phone
Open the address above in **Chrome** → **⋮** menu → **Add to Home screen** (or **Install app**) → **Install**.

iPhone (for people you share with): open in **Safari** → **Share** → **Add to Home Screen**.

## 3. Turn on delay alerts (free TomTom key)
1. Go to **developer.tomtom.com** and register (free, no credit card).
2. In your dashboard, open the API keys page and copy your key.
3. In the app tap **⚙** → paste the key → **Save & test**. It should say "Key works."

## Using it
- Pick **Commute** or **Jacksonville**, then your direction.
- **Top card**: the suggestion (commute) or a summary of problems ahead (trip).
- **Section strip**: green / yellow / red blocks between crossovers or cities. Tap one to jump to its cameras.
- **Problem cards**: what TomTom reports, how long ago it started, plus the camera **at the problem** and at the **back of the backup**. A pink **NEW & SERIOUS** badge means a crash or closure under 45 minutes old. That is the case where "10 minutes" can turn into 45, so look at the camera.
- **↻ Refresh** reloads images and delays. Images also refresh every 90 seconds, and delays every 5 minutes, but only while the app is open on screen.

## Updating later
Upload the new `index.html` (and any changed files) to the same repo. Phones pick up the update the next time the app is opened with a connection.

## Notes
- The camera list loads live from FDOT each day. If that fails, a built-in copy (Nov 24, 2026) is used.
- FDOT's "direction" field is unreliable in some counties (almost everything is listed as "N"), so treat "points your way" as a hint.
- FL511 content is for individual personal use. Check FDOT's terms before sharing the app widely.
