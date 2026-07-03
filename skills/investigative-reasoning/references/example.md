# Worked example — Diagnostic mode with Socratic bracketing

**User query:** "Our API error rate jumped from 0.1% to 4% at 2:14 PM. Nobody deployed
anything. Figure out what happened."

**Mode:** Socratic first (clarify), then abductive diagnostics, then Socratic validation.

---

**Socratic clarification (answered from available evidence, flagged where open):**

- What exactly errors? → 5xx responses from the orders service; other services nominal.
- "Nobody deployed" — does that include config, infra, and dependencies, or only
  application code? → Only app code confirmed. Config and infra changes: **open**.
- Is 2:14 PM sharp or a ramp? → Sharp step, per the dashboard.

**Observation:** Orders service 5xx rate stepped from 0.1% to 4% at 2:14 PM.
**Expectation:** Error rate stays ~0.1% absent a change.
**Gap:** Something changed at 2:14 PM that is not an application deploy.

**Ontology (constrains the hypothesis space):**
- Entities: orders service, its database, payment gateway (external), config store,
  TLS certificates, load balancer, DNS, deployment system.
- Valid relationships: reads-from, writes-to, depends-on, routes-to, expires-at,
  triggered-by.
- Invalid leap example: "the dashboard change caused the errors" — dashboards observe,
  they hold no valid causal relationship to request handling.

**Hypotheses (broad first, then constrained):**

1. **Proximate:** A scheduled config push or feature-flag change landed at 2:14 PM.
   Flags flip without "deploys."
2. **Proximate:** A TLS certificate or credential used by the orders service expired
   at 2:14 PM (expiry is time-triggered — fits a sharp step with no deploy).
3. **Environmental:** The external payment gateway degraded at 2:14 PM; orders
   surfaces its failures as 5xx.
4. **Systemic:** A database connection pool exhausted after slow growth — but this
   predicts a ramp, not a step. Weakened by the sharp-step evidence.

**Ranking (fewest unsupported assumptions, consistent with a sharp step and no deploy):**
(1) config/flag change — requires only that a push occurred, directly checkable;
(2) expiry — requires only a cert/credential with that expiry timestamp;
(3) gateway degradation — requires an external event we haven't observed;
(4) pool exhaustion — contradicts the step shape. Deprioritized.

**Verification steps:**
1. Diff the config store and flag audit log for changes in the 2:10–2:15 PM window.
2. List certs/credentials the orders service holds; check expiry timestamps.
3. Check the payment gateway's status feed and the error breakdown — are the 5xxs
   concentrated on payment-touching endpoints?

**Socratic validation of the leading hypothesis:** If a flag flipped at 2:14 PM, the
errors should be confined to code paths behind that flag, and flipping it back should
restore the 0.1% baseline immediately. If errors span unrelated endpoints, promote
hypothesis 2.

---

Note the shape: clarifying questions were answered, not just posed, and the open one
("config changes?") directly became hypothesis 1; the ontology ruled a tempting leap
out before hypotheses were generated; four hypotheses spanned proximate, systemic, and
environmental causes; ranking was by unsupported assumptions, not generation order; and
every surviving hypothesis carries a concrete check.
