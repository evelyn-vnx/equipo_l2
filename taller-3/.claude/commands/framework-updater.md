# Framework Updater

**Slash command:** `/framework-updater`
**Phase:** meta
**Model:** Claude Sonnet 4.6 (tier: standard)
**Tools:** runCommand, read, edit, search

## Description

Pulls latest versions of tracked public framework repositories, detects changes since the last refresh, and updates WHATSNEW.md. For major changes, delegates to framework-analyst and framework-comparator. Does NOT produce comparison documents from scratch.

## Instructions

- .sdd-modules/modules/sdd-evolution/instructions/framework-repos.instructions.md

## Handoffs

*(none)*
