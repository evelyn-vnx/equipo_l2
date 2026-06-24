        # Refactoring

        **Slash command:** `/refactoring`
        **Phase:** 5b
        **Model:** Claude Sonnet 4.6 (tier: standard)
        **Tools:** read, search

        ## Description

        Analyzes code against constitution principles and specification artifacts. Identifies tech debt, architecture violations, and improvement opportunities. Produces a structured refactoring plan with full traceability. Runs in Phase 5 alongside Review, or on-demand for existing codebases.

        ## Instructions

        - .github/instructions/anti-patterns.instructions.md
- .github/instructions/constitution-reading.instructions.md

        ## Handoffs

        - **Implement Refactoring** → `software-engineer`
- **Re-review After Refactoring** → `review`
