# Product Requirements Document: The "CapEx Whisperer" Agent

## 1. Executive Summary
The **CapEx Whisperer** is an agentic tool designed for Product Managers in legacy "Industrial" organizations (Airlines, Mining, Energy). It solves the "Digital CapEx Trap" by translating agile, experiment-based software needs into the rigid, asset-heavy financial language required by Investment Committees.

## 2. Job to be Done (JTBD)
**Context:** Ruslan (PM) needs to hire 2 devs for 3 months ($40k) to test a feature.
**Trigger:** Finance rejects the request because it lacks a "10-Year Asset Depreciation Schedule."
**The Job:** "Help me secure funding for this agile experiment by reframing it as a compliant 'Capital Asset' or 'Essential Maintenance' project so that I can bypass the Investment Committee rejection."

**Success Criteria:**
*   Approvals obtained < 5 days.
*   Zero "Investment Memos" written from scratch.
*   "Fraud Score" = 0 (Uses legitimate accounting classifications, not lies).

## 3. User Persona: Ruslan
*   **Pain:** Hates bureaucracy, feels misunderstood by Finance ("They count rivets, I write code").
*   **Need:** Speed and a "hack." He wants the "Magic Words" that make Finance say yes.
*   **Input Style:** "I need to fix the login flow."
*   **Desired Output:** A 10-page memo calculating the "Net Present Value of User Auth Asset Preservation."

## 4. Functional Requirements

### F1: The "Assetization" Translator
*   **Description:** Translates software engineering tasks into GAAP-compliant "Capital Asset" terminology.
*   **User Input:** "Refactoring the backend code to reduce latency."
*   **Agent Logic:** "Refactoring" = OpEx (Maintenance) -> Rejected. "Extending Useful Life" = CapEx (Investment) -> Approved.
*   **Agent Output:** "Strategic initiative to extend the useful economic life of the Core Digital Booking Engine (Asset #884) by 3 years, qualifying for amortization under IAS 38 (Intangible Assets)."

### F2: The "Authority Limit" Loophole Finder
*   **Description:** Scans internal policy documents to find the "check size" that avoids full committee review.
*   **User Input:** "Budget is $60k."
*   **Agent Action:** Checks uploaded "Procurement Policy.pdf". Finds that "projects under $50k" only need VP approval.
*   **Agent Output:** "Ruslan, if you scope this down to $49,500 by removing the 'Dark Mode' feature, you can bypass the Investment Committee entirely under Policy Clause 4.2a (Small Works)."

### F3: The ROI Proxy Generator
*   **Description:** Generates defensible financial projections for features that don't satisfy "Contracted Revenue" criteria.
*   **User Input:** "It's just a disruption tool, it doesn't make money directly."
*   **Agent Logic:** Disruption Tool = Lower Call Center Volume = Cost Saving.
*   **Agent Output:** "Projected Savings: 5,000 calls deflected @ $4/call = $20,000/month. Annual Impact: $240k. 3-Year NPV: $650k. ROI: 400%."

### F4: The "Threat" Framework
*   **Description:** Frames not doing the project as a "Risk" rather than a "Missed Opportunity" (Industrial Boards fear Risk more than they greed for Opportunity).
*   **User Input:** "We should do this to be modern."
*   **Agent Output:** "Failure to implement this update creates a Compliance Risk regarding Passenger Rights Legislation (Rule 261/2004), potentially exposing the airline to regulatory fines."

## 5. User Interface (Chat Interaction)
**Ruslan:** "I need money for the flight change bot."
**Agent:** "Okay. Is this a **New Asset** or **Maintenance**? (Hint: Maintenance is OpEx and will kill your EBITDA. Let's frame it as an 'Enhancement' to capitalize it.)"
**Ruslan:** "Enhancement."
**Agent:** "Great. Give me the estimated reduction in call center minutes, and I will generate the 'Section 7: Guaranteed Revenue' paragraph."

## 6. Technical Constraints
*   **Knowledge Base:** Must ingest IFRS/GAAP accounting standards regarding "Intangible Assets."
*   **Tone:** Professional/Financial in generated documents; Conspiratorial/Helpful in chat with Ruslan.
