# Research Agenda: AI Academic Integrity in Vietnamese Higher Education

**Prepared by:** EdTech Research Group, Nhập môn Khoa học Giáo dục (25CGD), HCMUS, Semester 2 2025-2026

**Basis:** Nine-position debate corpus, four-round debate transcript, critical gaps analysis, and post-debate supplement. This agenda translates the debate's empirical gaps into a prioritized, actionable research program for Vietnamese EdTech researchers, MOET working groups, and international collaborators.

**Organizing principle:** Studies are prioritized by *policy-relevance × evidence-gap severity × feasibility*. Tier 1 studies are needed before major policy decisions can be made with confidence. Tier 2 studies are needed to evaluate policies once implemented. Tier 3 studies are longer-horizon research with structural importance.

---

## Tier 1: Immediate Priority — Required Before Major Policy Decisions

These gaps directly undermine the evidentiary basis of the debate's consensus recommendations. Policy action is proceeding on inference; these studies would convert inference to evidence.

---

### Study 1: Vietnamese-Language AI Detection Tool Validation

**The gap:** The entire debate's red line against sole-evidence AI detection rests on Liang et al. (2023), which tested TOEFL essays by Chinese college students. Vietnamese students writing in Vietnamese-medium instruction, or producing Vietnamese-influenced English, are not in that sample. The 61.3% false positive figure is an inference applied to a different population. Whether Vietnamese students face equivalent, greater, or lesser false positive risk is unknown.

**Research question:** What are the actual false positive and false negative rates of GPTZero, Turnitin AI Detection, and Copyleaks when applied to (a) authentic Vietnamese-medium student writing, (b) Vietnamese students' English-medium academic writing, and (c) AI-generated text translated from Vietnamese?

**Methodology:**
- Corpus construction: collect authenticated human-written essays from Vietnamese students across disciplines and proficiency levels (requires institutional IRB and student consent). Minimum N=500 per category.
- AI-generated comparison corpus: generate matched essays using GPT-4o, Claude 3.5 Sonnet, and Gemini 2.0 on identical prompts.
- Run all three detection tools on both corpora. Measure false positive rate (human text flagged as AI), false negative rate (AI text not flagged), and sensitivity to language of composition (Vietnamese vs. Vietnamese-accented English vs. translated AI text).
- Stratify by discipline (STEM vs. social sciences vs. humanities), English proficiency level, and institution type (public research university vs. regional college vs. private institution).

**Who should conduct it:** VNU Hanoi or HCMUS research team in partnership with a detection tool provider willing to allow independent testing. International partner (e.g., Queensland University of Technology's academic integrity research group) for methodological validity.

**Estimated feasibility:** High. Corpus collection is the main cost. Student consent protocols are standard. No specialized equipment required. Timeline: 12-18 months.

**Policy decision it enables:** Whether the MOET prohibition of native-English-trained detection tools in Vietnamese proceedings (Recommendation 6, final_report.md) is justified by documented Vietnamese-specific harm or only by extrapolation from Chinese TOEFL data. Also whether Vietnamese-language detection tools, if developed, would face the same false positive problems.

---

### Study 2: Vietnamese Student AI Use Motivation Survey

**The gap:** The Springer 2024 study (N=1,386, list experiment methodology) established that AI fraud prevalence is approximately 3x the self-reported rate. It did not measure *why* students use AI fraudulently. The debate's policy prescriptions — structural reform, assessment redesign, honor code culture — each assume a different dominant motivation. Without motivation data, the prescriptions are guessing at causes.

**Research question:** Why do Vietnamese university students use AI tools in ways that violate institutional academic integrity policies? What is the relative prevalence of: (a) time pressure and workload overload, (b) lack of subject comprehension, (c) unclear or absent AI use policies, (d) low perceived detection risk, (e) belief that AI use is not cheating, (f) financial or employment pressure, (g) peer normalization?

**Methodology:**
- Mixed methods: online survey (N≥600) using validated academic dishonesty motivation scales (adapted from Anderman & Murdock 2007; Hensley et al. 2013) plus semi-structured interviews (N=30-40) for depth.
- Survey uses list experiment methodology (as in Springer 2024) to bypass self-report bias on sensitive items.
- Stratify by: institution type, year of study, discipline, AI use frequency, whether student has received institutional AI policy communication.
- Interview sample deliberately includes: students who self-report AI fraud, students who report classmates, students who received false positive accusations.

**Who should conduct it:** Vietnamese researcher with IRB access at a major public university. HCMUS EdTech faculty or VNU social science research center. Potential funding: NAFOSTED (National Foundation for Science and Technology Development), or ADB Vietnam education grants.

**Estimated feasibility:** Moderate-high. Survey instrument adaptation is straightforward. Student recruitment via institutional channels is feasible with faculty cooperation. Timeline: 12 months.

**Policy decision it enables:** Whether the primary intervention should target structural workload (Left-Wing prescription), incentive recalibration (Economist prescription), assessment design (Educator prescription), or policy communication (all positions agree this is necessary). Motivation data is the causal map the policy prescriptions need.

---

### Study 3: Spot Viva Effectiveness RCT

**The gap:** The debate's primary recommendation — spot viva (oral defense) sampling — is endorsed by all nine positions, but the empirical evidence base is thin: one institution (University of Western Ontario), anecdotal reports from Macquarie Law School, and the BUV AIAS pilot (which did not isolate the viva component's contribution). The Economist's deterrence math was challenged in the debate supplement on game theory grounds (10% sampling may be below deterrence threshold for rational actors). No RCT exists.

**Research question:** Does 15% random spot viva sampling produce a statistically significant reduction in AI fraud rates compared to (a) traditional assessment alone and (b) traditional assessment plus AI detection tool advisory use?

**Methodology:**
- Three-arm RCT across matched course sections at 2-3 Vietnamese universities:
  - Arm A: Traditional assessment only (control)
  - Arm B: Traditional assessment + AI detection tool used as soft advisory signal (not disciplinary evidence)
  - Arm C: Traditional assessment + 15% random spot viva sampling
- Outcome measurement: AI fraud prevalence via list experiment methodology (not self-report) at end of semester. Secondary outcomes: student-reported stress levels, perceived fairness, and instructor workload.
- Randomization unit: course section (to avoid contamination within cohort).
- Minimum N: 150 students per arm (power calculation: detect 15 percentage point difference at α=0.05, β=0.80).

**Who should conduct it:** HCMUS or VNU faculty consortium. Requires institutional approval and faculty cooperation across multiple departments. Methodology expertise in list experiment design needed (contact Springer 2024 authors for collaboration).

**Estimated feasibility:** Moderate. The main constraint is institutional willingness to randomize — universities may resist being in the "no viva" control arm. Can be designed as a phased rollout RCT (all arms eventually receive the intervention) to reduce this resistance. Timeline: 18-24 months for one academic year of data.

**Policy decision it enables:** Whether spot viva is worth the faculty time investment at scale, what sampling rate produces reliable deterrence, and whether the Economist's NPV calculation holds in the Vietnamese institutional context.

---

## Tier 2: Medium-Term — Required to Evaluate Policy Implementation

These studies are needed once policies from the final_report.md framework are implemented. Without them, Vietnam cannot know whether the interventions are working or at what cost.

---

### Study 4: Total Academic Dishonesty Baseline — Pre- and Post-AI Comparison

**The gap:** The debate assumed AI fraud represents a net increase in academic dishonesty. The Adaptive Minimalism position challenged this: students may be substituting AI fraud for essay mill fraud with no net increase in total dishonesty. Without a pre-ChatGPT baseline using equivalent methodology, the "crisis" frame cannot be validated or falsified. Sheffield's 15x increase measures *reported cases*, not fraud prevalence — an artifact of changed detection behavior.

**Research question:** Has total academic dishonesty (AI fraud + essay mill/contract cheating + traditional copying) in Vietnamese universities increased since November 2022, compared to the 2019-2022 baseline period, when measured using equivalent methodology?

**Methodology:**
- Longitudinal list experiment survey administered in 2026 and again in 2028, measuring total academic dishonesty rate across all modalities.
- Compare 2026 data to Springer 2024 data (which measured AI fraud prevalence, not total dishonesty) using the same list experiment format.
- Retrospective component: ask 2026 respondents to report retrospective academic dishonesty behavior from 2020-2022 period (caveat: recall bias; treat as supplementary, not primary evidence).
- Track essay mill service usage in parallel (web analytics, survey) to detect substitution effects.

**Who should conduct it:** Same team as Study 2, building on established survey infrastructure. Springer 2024 author collaboration highly recommended for methodological continuity.

**Estimated feasibility:** High (given Study 2 infrastructure). Primary cost is longitudinal panel maintenance. Timeline: 2026 wave (12 months from funding) + 2028 wave.

**Policy decision it enables:** Whether the urgency of emergency regulatory response is justified by a demonstrated net increase in academic dishonesty, or whether the debate's consensus is responding to a shift in *form* rather than an increase in *prevalence*. This directly addresses the Adaptive Minimalism challenge to Claim 1.2.

---

### Study 5: Cost-Benefit Analysis of Assessment Redesign in Vietnamese HE

**The gap:** The Economist's position endorses assessment redesign as positive-NPV investment, but the supporting numbers are thin: "10 hours per 300-student cohort" for spot viva is an estimate, not a measurement. No published study documents the actual institutional cost of redesigning assessment at scale in a Vietnamese context — faculty time, TA training, scheduling infrastructure, and the opportunity cost of assignments replaced.

**Research question:** What is the actual cost (faculty time, infrastructure, training) and benefit (misconduct reduction, student learning outcomes, faculty satisfaction) of implementing the AIAS framework at scale across a Vietnamese public university?

**Methodology:**
- Partner with 3-5 Vietnamese universities implementing AIAS (building on BUV pilot).
- Time-and-motion study: track faculty hours in assessment redesign (Year 1), pilot implementation (Year 2), and scaled deployment (Year 3).
- Measure outcomes: AI misconduct rate (list experiment), student learning outcomes (standardized assessment), faculty satisfaction (validated survey), administrative burden (hours per semester).
- Cost comparison: document actual Turnitin subscription costs and adjudication time at comparison institutions not implementing AIAS.

**Who should conduct it:** HCMUS EdTech faculty with MOET cooperation. BUV (British University Vietnam) as implementation partner — they have the AIAS pilot data and Perkins as PI. Potential funding: British Council Vietnam, ADB education sector grants.

**Estimated feasibility:** Moderate. Requires faculty cooperation and longitudinal commitment from participating institutions. The main risk is implementation fidelity variation across sites. Timeline: 3 years (one per implementation phase).

**Policy decision it enables:** Whether Recommendation 12 (invest in oral defense infrastructure, not detection infrastructure) is cost-justified in Vietnamese public university contexts with high student-to-faculty ratios. The Economist's positive-NPV claim needs Vietnamese-context numbers to be actionable for MOET budget allocation.

---

### Study 6: McCabe Honor Code Cross-Cultural Validity

**The gap:** The final_report.md elevates McCabe's 25-30% cheating reduction finding as "the most important single datum in the long-run literature," but McCabe's sample is US institutions with specific self-selection properties (West Point, UVA, Rice). Cultural transferability to Vietnam's Confucian-influenced, hierarchical educational culture — where peer reporting carries high social cost and collective student solidarity works against whistleblowing — has never been tested.

**Research question:** Does deliberately building honor code culture in Vietnamese universities produce cheating rate reductions comparable to McCabe's 25-30% finding, or does the effect size differ substantially due to cultural and institutional differences?

**Methodology:**
- Quasi-experimental design: identify 4-6 Vietnamese universities willing to implement structured honor code programs (student pledge, faculty modeling, integrity education modules, voluntary reporting mechanisms adapted for Vietnamese face-saving culture).
- Comparison institutions: matched universities not implementing honor code programs.
- Outcome: AI fraud and total dishonesty prevalence (list experiment) at baseline, 1 year, and 3 years post-implementation.
- Process evaluation: document which specific mechanisms produce norm change in Vietnamese context — is peer reporting culturally viable, or do liêm sỉ-based mechanisms (collective shame, faculty moral authority) produce equivalent effects?

**Who should conduct it:** Vietnamese education psychologists + McCabe's research group (ICAI, Clemson University) as methodological partner. ICAI has conducted cross-national honor code research and would have strong interest in Vietnamese data.

**Estimated feasibility:** Moderate. Requires 3-year commitment and institutional partners willing to implement honor code programs. The cultural adaptation of the intervention is itself a research contribution. Timeline: 4 years (1 year adaptation + 3 years measurement).

**Policy decision it enables:** Whether Recommendation 15 (honor code culture development) should be stated as "expected to produce 25-30% reduction" or "expected to produce positive but culturally-contingent reduction." Also identifies which specific mechanisms work in Vietnamese contexts.

---

### Study 7: Longitudinal AIAS Impact Study at BUV and Comparable Institutions

**The gap:** BUV's AIAS pilot demonstrated measurable misconduct reduction during the implementation period. Three questions remain: (a) does the improvement persist after novelty effects dissipate, (b) does it scale to institutions without Perkins-level implementation leadership, and (c) does it transfer across Vietnamese institutional types (public research university vs. regional college vs. private institution)?

**Research question:** Do AIAS framework implementations produce sustained, scalable, and transferable reductions in AI misconduct across diverse Vietnamese HE contexts over a 3-5 year horizon?

**Methodology:**
- Follow-up panel study at BUV: continue measuring AI misconduct prevalence annually through 2028-2029. Test for novelty decay.
- Comparative case studies: document AIAS implementations at 3-4 additional Vietnamese institutions varying in: size, public/private status, discipline mix, faculty capacity. Measure outcomes using consistent list experiment methodology.
- Implementation fidelity measurement: document which AIAS components are actually implemented versus which are adopted nominally.

**Who should conduct it:** Perkins and BUV research team as lead. HCMUS EdTech faculty as Vietnamese public university partner. Publication target: *International Journal for Educational Integrity* (IJEI) or *Computers & Education*.

**Estimated feasibility:** High — BUV pilot infrastructure exists, Perkins is motivated to publish longitudinal follow-up. The comparative case study component requires additional institutional partners. Timeline: ongoing, with major publication milestones at Year 3 and Year 5.

**Policy decision it enables:** Whether MOET's Recommendation 9 (AIAS adoption mandate) should be implemented immediately based on BUV evidence alone, or whether a phased pilot program with evaluation is required before nationwide mandate.

---

## Tier 3: Longer-Horizon — Structural Research for 2028-2035

These studies address the structural forces shaping the long-run landscape. They inform the 10-year policy frame, not immediate MOET decisions.

---

### Study 8: Credential Signal Degradation Study

**The gap:** The Economist's most consequential long-run prediction — that AI fraud will trigger Akerlof's lemons dynamic, causing employers to discount Vietnamese university credentials — is theoretically well-founded but empirically unstudied. If the prediction is correct, the social cost of unchecked AI fraud is dramatically larger than the direct academic harm.

**Research question:** Are Vietnamese employers already discounting university credentials in response to perceived AI fraud, and if so, how does this interact with the existing brain drain dynamic?

**Methodology:**
- Employer survey (N≥200 Vietnamese firms across sectors): measure credential confidence, verification behavior, and hiring practice changes since 2022.
- Longitudinal wage premium study: compare graduate wage premiums (credential return) from 2019-2022 vs. 2024-2027 using Vietnam Household Living Standards Survey data.
- Qualitative interviews with HR managers at firms with documented AI fraud concerns.

**Who should conduct it:** Vietnamese economists at CIEM (Central Institute for Economic Management) or Fulbright University Vietnam. Funding: World Bank Vietnam office, which already funds education economics research in Vietnam.

**Estimated feasibility:** Moderate. Employer survey is feasible; longitudinal wage data requires VHLSS access which requires MOLISA collaboration. Timeline: 2-3 years.

---

### Study 9: Open-Source LLM Proliferation Impact Study

**The gap:** The Technologist's prediction — that locally-run open-source models will make all detection and watermarking schemes functionally obsolete by 2028 — is the most consequential technical claim in the debate. If correct, it fundamentally changes the investment calculus: detection infrastructure being purchased in 2026 will be worthless by 2028. If incorrect, the watermarking mandate advocacy (Recommendation 13) has more time value.

**Research question:** At what rate are Vietnamese university students adopting locally-run open-source LLMs (Llama, Mistral, Qwen, Vistral) for academic work, and does this adoption rate follow the Technologist's timeline prediction?

**Methodology:**
- Annual survey of Vietnamese university students (N≥500) measuring: which AI tools they use for academic work, whether they use API-based tools (GPT-4, Claude) or locally-run models, and whether their tool choice is influenced by detection avoidance.
- Technical capability tracking: monitor minimum hardware requirements for running capable open-source models vs. Vietnamese student device ownership data.
- First wave: 2026. Annual follow-up through 2028. The prediction is falsifiable by 2028.

**Who should conduct it:** HCMUS computer science faculty with EdTech collaboration. Low cost (survey infrastructure only). Timeline: 2026-2028, with annual reports.

**Policy decision it enables:** Whether Recommendation 12's watermarking advocacy remains worth pursuing as open-source proliferates, and when the tipping point occurs at which detection-based approaches become fully obsolete.

---

### Study 10: Tự Chủ Đại Học and Research Integrity Incentive Study

**The gap:** RW and LW converged in Round 4 on a concern that tự chủ đại học (university autonomy) reform, by introducing performance management frameworks tied to publication targets and international rankings, may be generating domestic publish-or-perish pressures analogous to the Hindawi retraction dynamic at the institutional level. This mechanism has not been studied in Vietnamese HE.

**Research question:** Do Vietnamese universities that have adopted greater autonomy (under the 2018 Law on Higher Education amendments) show higher rates of research integrity problems — AI fraud in publications, citation manipulation, paper mill submissions — than universities under traditional ministry oversight?

**Methodology:**
- Quasi-experimental design: compare research integrity indicators (retraction rates, citation anomaly patterns, COPE complaint rates) between high-autonomy and low-autonomy Vietnamese universities, controlling for institution size and research output level.
- Survey of Vietnamese faculty: measure perceived publication pressure, clarity of institutional research integrity policies, and knowledge of COPE/ICMJE AI authorship guidelines.
- Document analysis: review promotion and tenure criteria at high-autonomy vs. low-autonomy institutions for publication volume requirements.

**Who should conduct it:** Vietnamese higher education policy researchers at SEAMEO RETRAC or VNU's higher education research center. MOET Higher Education Department as data access partner.

**Estimated feasibility:** Moderate. Retraction data is publicly available (Retraction Watch). Faculty survey feasibility depends on institutional cooperation. Timeline: 2-3 years.

---

### Study 11: Administrative Law Analysis — Surveillance Infrastructure Reuse Risk

**The gap:** The debate supplement identified that surveillance infrastructure built for academic integrity (writing process logging, behavioral monitoring, keystroke dynamics) cannot be adequately protected against non-educational reuse by Vietnamese state actors through academic integrity policy alone. This is a constitutional and administrative law question, not an educational research question.

**Research question:** Under current Vietnamese constitutional and administrative law, what legal protections prevent student behavioral data collected for academic integrity purposes from being accessed by state security actors, and are these protections adequate?

**Methodology:**
- Legal doctrinal analysis: review Vietnamese Constitution (2013, Articles 21-22 on privacy), Cybersecurity Law 2018, Decree on Personal Data Protection 2023, and Law on Higher Education for provisions governing student data access by state actors.
- Comparative analysis: how do comparable jurisdictions (Singapore, South Korea, Thailand) legally protect academic behavioral data from state access?
- Expert consultation: Vietnamese administrative law scholars and civil society organizations (IPS Vietnam, ISEAS-Yusof Ishak Institute).

**Who should conduct it:** Vietnamese law faculty (HCMC University of Law, VNU Faculty of Law) or international researchers with Vietnam law expertise. This is a desk research study — no fieldwork required.

**Estimated feasibility:** High for legal doctrinal analysis. Findings may be politically sensitive; publication venue selection requires care. Timeline: 6-12 months.

**Policy decision it enables:** Whether Recommendation 5b (surveillance infrastructure lock-in assessment) can be operationalized into specific legal due diligence requirements, or whether the risk is structural and cannot be mitigated by policy design alone.

---

## Summary Table

| Study | Tier | Primary gap addressed | Feasibility | Timeline | Who |
|---|---|---|---|---|---|
| 1. Vietnamese detection validation | 1 | Liang et al. scope | High | 12-18 mo | HCMUS + VNU |
| 2. Student motivation survey | 1 | Why students cheat | High | 12 mo | HCMUS EdTech |
| 3. Spot viva RCT | 1 | Viva evidence base | Moderate | 18-24 mo | Faculty consortium |
| 4. Total dishonesty baseline | 2 | Base-rate validation | High | 2 years | Springer 2024 team |
| 5. AIAS cost-benefit | 2 | Economist NPV claims | Moderate | 3 years | BUV + HCMUS |
| 6. McCabe cross-cultural | 2 | Honor code transferability | Moderate | 4 years | ICAI + VN partner |
| 7. AIAS longitudinal at BUV | 2 | Scalability/sustainability | High | 5 years | BUV/Perkins |
| 8. Credential signal degradation | 3 | Akerlof lemons prediction | Moderate | 3 years | CIEM/Fulbright VN |
| 9. Open-source LLM proliferation | 3 | Technologist's 2028 prediction | High | 2 years | HCMUS CS |
| 10. Tự chủ + research integrity | 3 | Autonomy reform risks | Moderate | 3 years | SEAMEO/VNU |
| 11. Administrative law analysis | 3 | Surveillance reuse risk | High | 6-12 mo | VN law faculty |

---

## Research Coordination Recommendations

**Immediate action (2026):** Studies 1, 2, and 9 can be initiated with existing Vietnamese university research infrastructure at low cost. Study 1 is the most urgent — it is the foundational empirical question underlying the detection consensus. Study 2 is the foundational empirical question underlying the policy prescriptions.

**Funding pathways:**
- NAFOSTED (National Foundation for Science and Technology Development): Studies 1, 2, 4, 10
- British Council Vietnam Higher Education Links: Studies 5, 6, 7 (BUV partnership)
- ADB Vietnam education sector grants: Studies 3, 5
- World Bank Vietnam: Study 8
- Internal HCMUS research fund: Studies 9, 11 (desk research; low cost)

**International collaboration priority:** Studies 3 (Springer 2024 methodology authors), 6 (ICAI/McCabe research group), and 7 (BUV/Perkins) have natural international partners who would benefit from Vietnamese-context data and could bring methodological expertise and publication credibility.

**What to avoid:** Commissioning studies 8-11 before studies 1-3 are complete. The structural questions only matter if the immediate empirical gaps are not resolved by evidence that changes the policy frame entirely. Study 1 (Vietnamese detection validation) could in principle either confirm or substantially revise the debate's primary red line; that revision should precede long-horizon structural research investments.

---

*Research agenda prepared for Nhập môn Khoa học Giáo dục (25CGD), HCMUS, Semester 2 2025-2026.*
*Grounded in: critical_gaps.md, debate_supplement.md, final_report.md (nine-position revised version).*
*Primary audience: Vietnamese EdTech researchers, MOET Higher Education Department, international academic integrity research partners.*
