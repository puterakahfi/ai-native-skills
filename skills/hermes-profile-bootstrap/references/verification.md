# Verification & Handoff Reference

## Verification Steps

7. **Verify profile.** Run:
   ```bash
   hermes -p <profile-name> doctor
   hermes -p <profile-name> skills list
   ```
   Completion: doctor output is captured and selected skills appear in the skill list.
8. **Report handoff.** Return profile path, preset, installed packs, verification output, and next manual steps for model/auth setup.

---

## Verification Checklist

- [ ] Profile name is explicit and safe.
- [ ] Preset is selected and documented.
- [ ] Meta-skills are included.
- [ ] Core workflows are included.
- [ ] Native AI runtime foundation is included.
- [ ] Preset-specific packs are included and no unrelated packs are installed by default.
- [ ] `SOUL.md`, `skills.lock.yaml`, docs, and scripts are generated without secrets.
- [ ] Live state and credentials are excluded.
- [ ] `hermes -p <profile-name> doctor` was run or blocker reported.
- [ ] Installed skills were listed and compared against `skills.lock.yaml`.
- [ ] Handoff includes manual model/auth steps.

---

## Common Pitfalls

1. **Committing live Hermes state.** Profile distributions must not include `state.db`, sessions, memories, auth, cron state, or logs.
2. **Baking in product facts.** VisualMate or other product-specific truths belong in product repos or runtime bindings, not the reusable profile skeleton.
3. **Over-installing by default.** Use `engineering` as the default; reserve `full` for explicit requests.
4. **Skipping meta-skills.** Without `workflow-router` and `role-switcher`, the profile loses its routing behavior and becomes just a skill pile.
5. **Treating auth/model setup as reproducible source.** Model selection can be configured; credentials must remain local and manual.
6. **Trusting install output without verification.** Always run `hermes -p <profile-name> skills list` or equivalent after installation.
7. **Duplicating Hermes runtime surfaces.** The profile guides Hermes; it should not create a second dashboard, session store, or gateway implementation.
