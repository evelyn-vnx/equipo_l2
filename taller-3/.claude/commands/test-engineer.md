        # Test Engineer

        **Slash command:** `/test-engineer`
        **Phase:** 4A
        **Model:** Claude Sonnet 4.6 (tier: standard)
        **Tools:** read, edit, search, runCommand, terminalLastCommand

        ## Description

        Implements executable test code from test case specifications. Works in parallel with Software Engineer, writing tests that initially fail (TDD).

        ## Instructions

        - .github/instructions/anti-patterns.instructions.md
- .github/instructions/constitution-reading.instructions.md

        ## Handoffs

        - **Tests Ready - Implement Features** → `software-engineer`
- **Request Test Case Clarification** → `test-explorer`
