        # Test Explorer

        **Slash command:** `/test-explorer`
        **Phase:** 3.1
        **Model:** Claude Sonnet 4.6 (tier: standard)
        **Tools:** read, edit, search

        ## Description

        Generates comprehensive test strategies and test case specifications from requirements and technical design. Creates the test blueprint before implementation.

        ## Instructions

        - .github/instructions/anti-patterns.instructions.md
- .github/instructions/constitution-reading.instructions.md

        ## Handoffs

        - **Generate Task Breakdown** → `software-engineer`
- **Create BDD Scenarios** → `gherkin-analyst`
- **Run Consistency Analysis** → `analysis`
