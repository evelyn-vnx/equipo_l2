        # Architect

        **Slash command:** `/architect`
        **Phase:** 2.1
        **Model:** Claude Opus 4.6 (tier: deep)
        **Tools:** read, edit, search, runSubagent, fetch

        ## Description

        Converts clarified specifications into technical designs including architecture, data models, and component design. Ensures design satisfies all requirements and follows constitution principles.

        ## Instructions

        - .github/instructions/anti-patterns.instructions.md
- .github/instructions/constitution-reading.instructions.md

        ## Handoffs

        - **Define API Contracts** → `api-champion`
- **Define Messaging Contracts** → `messaging-champion`
- **Skip to Test Strategy** → `test-explorer`
