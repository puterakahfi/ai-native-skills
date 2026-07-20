# Targeted Conformance Findings

## Summary

- `Checked:       87 adapter skills`
- `Conformant:    13`
- `Warnings:      156`
- `Not checkable: 0`
- `Errors:        11`
- `FAIL — 11 conformance error(s).`

## Boundary findings (0)

_None._

## Error findings (11)

```text
✗ skills/api-contract/SKILL.md
  quality_gates [ERROR]: quality_gates coverage: 3/8 (38%)
    - api_must_have_explicit_versioning_strategy
    - breaking_changes_must_be_detected_before_deploy
    - no_undocumented_endpoints_in_production
    - backward_compatibility_must_be_preserved_within_major_version
    - deprecation_must_be_announced_before_removal

```

```text
✗ skills/content-strategy/SKILL.md
  quality_gates [ERROR]: quality_gates coverage: 0/2 (0%)
    - information_sequenced_by_user_mental_model
    - tone_consistent_across_sections

```

```text
✗ skills/data-modeling/SKILL.md
  quality_gates [ERROR]: quality_gates coverage: 1/3 (33%)
    - migrations_are_reversible_or_documented
    - no_implicit_coupling_across_bounded_contexts

```

```text
✗ skills/design-spacing/SKILL.md
  quality_gates [ERROR]: quality_gates coverage: 1/5 (20%)
    - rhythm_consistent_across_sections
    - ma_intentional_not_accidental
    - more_space_above_headings_than_below
    - no_min_height_100vh

```

```text
✗ skills/ethics-responsible-ai/SKILL.md
  quality_gates [ERROR]: quality_gates coverage: 2/8 (25%)
    - affected_groups_must_be_identified_before_launch
    - training_data_bias_must_be_audited
    - ai_involvement_must_be_disclosed_to_users
    - accountability_must_be_assigned_for_ai_errors
    - harm_must_be_assessed_not_assumed_negligible

```

```text
✗ skills/information-architecture/SKILL.md
  quality_gates [ERROR]: quality_gates coverage: 1/3 (33%)
    - nav_items_reflect_page_sections
    - max_2_nav_levels

```

```text
✗ skills/macrostructures/SKILL.md
  quality_gates [ERROR]: quality_gates coverage: 1/4 (25%)
    - new_pick_must_differ_from_prior_on_2_or_more_axes
    - no_dead_space_in_split_panels
    - cards_must_fill_height_in_split_layout

```

```text
✗ skills/motion-design/SKILL.md
  quality_gates [ERROR]: quality_gates coverage: 1/4 (25%)
    - every_animation_has_user_signal_purpose
    - hover_transitions_200ms_or_less
    - prefers_reduced_motion_media_query_present

```

```text
✗ skills/role-switcher/SKILL.md
  quality_gates [ERROR]: quality_gates coverage: 2/6 (33%)
    - intent_must_be_detected_before_role_selection
    - each_role_must_contribute_a_distinct_lens
    - multi_role_output_must_be_structured_by_lens
    - agent_must_state_which_roles_were_activated

```

```text
✗ skills/ui-components/SKILL.md
  quality_gates [ERROR]: quality_gates coverage: 0/2 (0%)
    - pattern_selected_from_decision_tree_not_arbitrary
    - hero_pattern_matches_content_volume

```

```text
✗ skills/web-performance/SKILL.md
  quality_gates [ERROR]: quality_gates coverage: 0/3 (0%)
    - lcp_under_2500ms
    - cls_under_0_1
    - no_render_blocking_resources

```
