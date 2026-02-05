# Product Requirements Document: Passenger Disruption Recovery Agent
**Project Code:** "Phoenix" (Automated Rebooking System)
**Owner:** Ruslan (Senior Product Manager)

## 1. Executive Summary
This is the "Agile Experiment" Ruslan is trying to fund. It is an AI-driven agent embedded in the Air Astana mobile app that automatically resolves passenger disruptions (cancellations/delays) without human intervention.
**Strategic Alignment:** Directly supports the Strategy Pillar "Efficiency" (Low Cost Base) and "Excellence" (Customer Experience).

## 2. Job to be Done (JTBD)
**Primary Persona:** The "Stranded Passenger"
*   **Trigger:** "My flight KC-XXX just got cancelled while I'm at the airport."
*   **Current State (Pain):** Panic. Must queue at a physical desk (2 hours) or call the contact center (45 min hold).
*   **The Job:** "Get me on the next best flight home immediately so I don't miss my meeting/family event."
*   **Success Metrics:**
    *   Time to Rebook: < 2 minutes.
    *   NPS Contribution: +5 points.

**Secondary Persona:** The "Overwhelmed Call Center Agent"
*   **The Job:** "Deflect routine rebooking calls during mass disruptions so I can focus on complex cases (minors, medical)."

## 3. Product Vision & Principles
*   **Proactive, not Reactive:** Push the solution before the user calls.
*   **Transparency:** Explain *why* the flight was cancelled (per Law on AI explainability).
*   **Fairness:** Do not prioritize high-status passengers for seats in a way that violates "Fair Treatment" laws.

## 4. Functional Requirements

### F1: The "Instant Offer" Engine
*   **Trigger:** Flight Status changes to "Cancelled" in the Operational Database.
*   **Action:** Algorithm identifies the 3 best alternative routes (considering partnerships).
*   **Output:** Push notification: "We are sorry. Your flight is cancelled. We have held a seat for you on KC-YYY departing in 3 hours. Confirm?"

### F2: Comp-and-Care Automation
*   **Context:** If delay > 2 hours.
*   **Action:** Automatically issue digital vouchers for food/hotel to the app wallet.
*   **Constraint:** Compliance with Aviation Law (Article 86 - Passenger Rights).

### F3: Refund vs. Rebook Logic
*   **Logic:** If no flights exist within 24 hours, offer instant full refund to original payment method.

## 5. Technical Architecture (The "CapEx" Argument)
To satisfy Finance, we define this not as "scripting" but as **"Building Digital Infrastructure"**:
*   **Core Asset:** "Disruption Logic Engine" (Capitalizable Intangible Asset).
*   **Integration:** Connects Amadeus (PSS) with the Mobile App API.

## 6. Success Metrics (Outcomes)
*   **Call Deflection:** 40% of disruptive contacts resolved in-app.
*   **Cost Savings:** Lower GDS fees + reduced Call Center overtime.
*   **Speed:** Average resolution time drops from 45 mins to 90 seconds.
