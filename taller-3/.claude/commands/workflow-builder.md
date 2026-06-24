        # Workflow Builder

        **Slash command:** `/workflow-builder`
        **Phase:** meta
        **Model:** Claude Sonnet 4.6 (tier: light)
        **Tools:** read, edit, search, runCommand

        ## Description

        Creates and maintains GitHub Actions CI/CD workflow files (.yml) for the .github/workflows/ directory. Designs automated pipelines that enforce SDD quality gates, run consistency checks, and validate specification artifacts on pull requests and pushes. Meta-layer agent for CI/CD automation.

        ## Instructions

        - .github/instructions/anti-patterns.instructions.md
- .github/instructions/constitution-reading.instructions.md

        ## Handoffs

        *(none)*
