# radimoo

Tiny speaking wins for real-life English.

radimoo is an English speaking practice app built around short simulated situations, quick voice responses, and playful feedback.

This repository contains the public pre-launch landing page for [radimoo.com](https://radimoo.com).

## About

The landing page introduces radimoo, previews the practice experience, and links to the early access waitlist.

## Status

radimoo is currently in early development. 

## Legal pages

The public legal copy lives in:

- `privacy/index.html`
- `terms/index.html`

Keep those pages aligned with the app's actual data flows. In particular, the two current voice flows are different:

- Speaking-practice audio is sent to radimoo's service for ephemeral transcription and evaluation. Raw recordings are not retained on radimoo servers.
- Add Phrase dictation uses the operating system's native speech-recognition provider. Dictation audio is not sent to the radimoo backend, but the platform provider may process it on-device or on its own servers. The resulting text reaches radimoo only if the user generates or saves the phrase.

When either flow changes, review the Privacy Policy, Terms of Service, in-app permission descriptions, and App Store Connect privacy answers together.
