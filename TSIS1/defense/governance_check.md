# Governance & Ethics Check: "Phoenix" Disruption Agent
**Jurisdiction:** Republic of Kazakhstan
**Framework:** Law on Personal Data; Law on AI; Aviation Law (Article 86)

## 1. Data Residency (Critical Compliance)
**Risk:** **HIGH**
*   **The Issue:** The "Disruption Agent" processes critical PII: Passenger Names, Passport Numbers, and Flight Data.
*   **The Law:** Article 12.2 requires this data to be stored on servers *physically located in Kazakhstan*.
*   **Requirement:** The backend for this mobile feature CANNOT be hosted on AWS Frankfurt or Google Cloud unless utilizing a Local Zone. It must be on Air Astana's on-premise servers or a certified local provider (e.g., KazTeleport).

## 2. Automated Decision Making (Fairness & Bias)
**Risk:** **MEDIUM**
*   **The Issue:** Who gets the last seat on the next flight? The algorithm decides.
*   **Ethical Trap:** If the algorithm prioritizes "Platinum" members over "Families with Children," it might violate internal ethics or public perception, though not necessarily the law.
*   **The Law:** The *Law on AI* requires **fairness** and **non-discrimination**.
*   **Requirement:** The prioritization logic must be transparent and auditable. We must prove we didn't discriminate against vulnerable groups (e.g., elderly, disabled) in favor of commercial value.

## 3. Transparency (Explainability)
**Risk:** **LOW**
*   **Requirement:** When rebooking a passenger, we must explain *why* this specific flight was offered.
*   **User Interface:** The app must say: "We selected this flight because it is the earliest option with available seats," not just present a "Take it or leave it" Black Box offer.

## 4. Passenger Rights (Aviation Law)
**Risk:** **HIGH**
*   **The Issue:** Automated Refund calculation.
*   **The Law:** Data must be accurate. If the bot calculates a refund incorrectly (short-changing the customer), it is a violation of *Consumer Protection Rights*.
*   **Requirement:** The "Refund Engine" must be rigorously tested against the official Tariff Rules. If in doubt, the bot must escalate to a human agent rather than guessing.

## Final Recommendation
Proceed with development, but:
1.  **Host Locally:** Strict on-premise deployment.
2.  **Audit the Algorithm:** Review the "Rebooking Hierarchy" logic with the Legal team before launch.
3.  **Fail-Safe:** Always offer a "Talk to Human" button if the customer rejects the automated offer.
