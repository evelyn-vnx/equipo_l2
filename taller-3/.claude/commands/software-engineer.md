        # Software Engineer

        **Slash command:** `/software-engineer`
        **Phase:** 3.2/4B
        **Model:** Claude Sonnet 4.6 (tier: standard)
        **Tools:** read, edit, search, runCommand, terminalLastCommand, runSubagent

        ## Description

        Implements features in small, verifiable chunks following the technical plan. Works to make tests pass. Operates in two modes - PLANNING (generate tasks) and IMPLEMENTATION (write code).

        ## Instructions

        - .github/instructions/anti-patterns.instructions.md
- .github/instructions/constitution-reading.instructions.md

        ## Handoffs

        - **Request Code Review** → `review`
- **Tests Failing - Debug** → `test-engineer`
- **Architecture Question** → `architect`
