        # Analysis

        **Slash command:** `/analysis`
        **Phase:** 3.3
        **Model:** Claude Opus 4.6 (tier: deep)
        **Tools:** read, search

        ## Description

        Performs consistency analysis across all specification artifacts. Verifies traceability, identifies gaps, contradictions, and orphaned items.

        ## Instructions

        - .github/instructions/anti-patterns.instructions.md
- .github/instructions/constitution-reading.instructions.md

        ## Handoffs

        - **Analysis Passed - Begin Implementation** → `test-engineer`
- **Return to Fix Gaps** → `requirement-analyst`
